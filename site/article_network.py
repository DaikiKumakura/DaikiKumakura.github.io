"""Unsupervised article similarity network, calculated from the supplied live corpus.

No article categories, manually assigned topics, filenames or publication times are
features. English metadata provides a common language; body features use Latin
words so Japanese-only bodies can contribute scientific names and abbreviations.
"""
from collections import Counter
from hashlib import sha256
from math import log, sqrt
from pathlib import Path
import json
import re
import unicodedata

import networkx as nx

SEED = 20261027
STOP = frozenset(line for line in (Path(__file__).parent / 'network-stopwords.txt').read_text(encoding='utf-8').splitlines() if line and not line.startswith('#'))


def words(text):
    text = unicodedata.normalize('NFKC', text).lower()
    return [word for word in re.findall(r'\b[a-z][a-z0-9]*(?:[-/][a-z0-9]+)*\b', text)
            if len(word) > 1 and word not in STOP]


def main_text(text):
    # Bibliographies, code, equations and destinations do not describe the question.
    text = re.split(r'^##\s+[^\n]*(?:文献|参考資料|出典|References|Sources)', text, maxsplit=1, flags=re.M | re.I)[0]
    text = re.sub(r'```[\s\S]*?```|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$', ' ', text)
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', text)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'https?://\S+|<[^>]+>|`[^`]+`', ' ', text)
    return text


def tfidf(documents):
    counts = [Counter(document) for document in documents]
    frequency = Counter(word for document in counts for word in document)
    vectors = []
    for count in counts:
        vector = {word: (1 + log(value)) * (1 + log((1 + len(counts)) / (1 + frequency[word])))
                  for word, value in count.items()}
        norm = sqrt(sum(value * value for value in vector.values()))
        vectors.append({word: value / norm for word, value in vector.items()} if norm else {})
    return vectors


def cosine(a, b):
    return sum(value * b.get(word, 0) for word, value in a.items())


def article_network(articles, links):
    articles = sorted((article for article in articles if not article['meta']['draft']), key=lambda a: a['slug'])
    records = []
    for article in articles:
        meta = article['meta']
        english = meta['locales'].get('en') or meta.get('english')
        # A missing English abstract does not stop an older site fixture building.
        abstract = english or meta['locales'][meta['source_language']]
        title = words(abstract['title'])
        summary = words(abstract['summary'])
        body = (article['folder'] / (meta['source_language'] + '.md')).read_text(encoding='utf-8')
        records.append({'id': article['slug'], 'title_terms': title, 'metadata': title * 2 + summary,
                        'body': words(main_text(body))})
    metadata = tfidf([r['metadata'] for r in records])
    bodies = tfidf([r['body'] for r in records])
    graph = nx.Graph()
    graph.add_nodes_from(range(len(records)))
    similarities = {}
    for i in graph:
        for j in range(i + 1, len(records)):
            similarities[i, j] = .65 * cosine(metadata[i], metadata[j]) + .35 * cosine(bodies[i], bodies[j])
    for i in graph:
        nearest = sorted(((similarities[min(i, j), max(i, j)], j) for j in graph if i != j), key=lambda pair: (-pair[0], pair[1]))[:3]
        for weight, j in nearest:
            if weight >= .08:
                graph.add_edge(i, j, weight=weight)
    if graph.number_of_edges():
        communities = nx.community.louvain_communities(graph, weight='weight', resolution=1, seed=SEED)
        modularity = nx.community.modularity(graph, communities, weight='weight')
    else:
        communities = [{i} for i in graph]
        modularity = 0
    communities = sorted(communities, key=lambda group: (-len(group), min(group)))
    positions = nx.spring_layout(graph, seed=SEED, weight='weight', iterations=200, scale=1) if records else {}
    clusters = []
    nodes = []
    for number, community in enumerate(communities, 1):
        # Contrast the centroid with the rest of the corpus to avoid generic labels.
        scores = Counter()
        for i in range(len(records)):
            coefficient = 1 / len(community) if i in community else -1 / (len(records) - len(community))
            for word, value in metadata[i].items():
                scores[word] += coefficient * value
        title_terms = {word for i in community for word in records[i]['title_terms']}
        terms = [word for word, _ in sorted(scores.items(), key=lambda pair: (-pair[1], pair[0])) if word in title_terms][:3]
        label = ' · '.join(terms) or 'No shared terms'
        slug = f'cluster-{number}'
        members = [records[i]['id'] for i in sorted(community)]
        clusters.append(dict(id=number, slug=slug, label=label, keywords=terms,
                             href=f'topics/{slug}.html', articles=members,
                             description='Automatically detected text-similarity community. Keywords are calculated from article titles and summaries; membership is recalculated when the published corpus changes.'))
        for i in sorted(community):
            record = records[i]; link = links[record['id']]
            nodes.append(dict(id=record['id'], title=link['title'], href=link['href'], lang=link['lang'],
                              cluster=number, x=round(400 + float(positions[i][0]) * 285, 4),
                              y=round(240 + float(positions[i][1]) * 175, 4)))
    edges = [dict(source=records[i]['id'], target=records[j]['id'], weight=round(data['weight'], 6))
             for i, j, data in sorted(graph.edges(data=True))]
    return dict(schema_version=1, corpus_sha256=sha256(json.dumps(records, sort_keys=True).encode()).hexdigest(),
                method=dict(features='TF-IDF; English title (counted twice) and summary, plus Latin-script words from original main text',
                            metadata_weight=.65, body_weight=.35, neighbors=3, minimum_similarity=.08,
                            graph='union of top-3 cosine neighbors above threshold',
                            clustering='weighted Louvain', resolution=1, seed=SEED,
                            labels='top three title terms by community-minus-rest title/summary TF-IDF centroid',
                            layout='weighted spring layout', networkx=nx.__version__),
                article_count=len(records), edge_count=len(edges), modularity=round(modularity, 6),
                clusters=clusters, nodes=nodes, edges=edges)
