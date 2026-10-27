"""Direct, unsupervised clustering of article titles and summaries."""
from collections import Counter
from hashlib import sha256
from math import log, sqrt
from pathlib import Path
import json
import re
import unicodedata
from topic_embeddings import embedding_vectors, MODEL, REVISION

LABEL_VERBS = frozenset('predict predicts understand understands improve improves compare compares change changes inform informs support supports separate separating matching'.split())
STOP = frozenset(line for line in (Path(__file__).parent / 'topic-stopwords.txt').read_text(encoding='utf-8').splitlines() if line and not line.startswith('#'))


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


def silhouette(groups, distances):
    total = 0.0
    for group in groups:
        for i in group:
            if len(group) == 1:
                continue
            within = sum(distances[i][j] for j in group if i != j) / (len(group) - 1)
            other = min(sum(distances[i][j] for j in candidate) / len(candidate)
                        for candidate in groups if candidate is not group)
            total += (other - within) / max(within, other) if max(within, other) else 0
    return total / len(distances)


def partition(distances):
    n = len(distances)
    if n < 3:
        return ([set(range(n))] if n else []), []
    active = {i: {i} for i in range(n)}
    pair = {(i,j): distances[i][j] for i in range(n) for j in range(i+1,n)}
    candidates = []
    next_id = n
    while len(active) > 1:
        a,b = min(pair,key=lambda key:(pair[key],key))
        na,nb = len(active[a]),len(active[b])
        combined = active[a] | active[b]
        updates = {}
        for c in active:
            if c in (a,b):continue
            updates[min(c,next_id),max(c,next_id)] = (na*pair[min(a,c),max(a,c)]+nb*pair[min(b,c),max(b,c)])/(na+nb)
        pair = {key:value for key,value in pair.items() if a not in key and b not in key}
        pair.update(updates)
        del active[a];del active[b];active[next_id]=combined;next_id+=1
        if 2 <= len(active) <= min(10,n-1):
            groups=list(active.values())
            candidates.append((silhouette(groups,distances),len(groups),[set(group) for group in groups]))
    best = max(candidates,key=lambda candidate:(candidate[0],-candidate[1]))
    groups = best[2] if best[0] > 0 else [set(range(n))]
    return groups,[dict(k=k,silhouette=round(score,6)) for score,k,_ in sorted(candidates,key=lambda candidate:candidate[1])]


def cluster_articles(articles, links):
    articles=sorted((a for a in articles if not a['meta']['draft']),key=lambda a:a['slug'])
    records=[];surfaces={}
    for article in articles:
        m=article['meta'];text=m['locales'].get('en') or m.get('english') or m['locales'][m['source_language']]
        title=words(text['title']);summary=words(text['summary'])
        raw=re.findall(r'\b[A-Za-z][A-Za-z0-9]*(?:[-/][A-Za-z0-9]+)*\b',text['title'])
        phrases=[]
        for a,b in zip(raw,raw[1:]):
            if a.lower() not in STOP and b.lower() not in STOP and a.lower() not in LABEL_VERBS and b.lower() not in LABEL_VERBS:
                term=a.lower()+' '+b.lower();phrases.append(term);surfaces.setdefault(term,Counter())[a+' '+b]+=1
        for word in raw:surfaces.setdefault(word.lower(),Counter())[word]+=1
        records.append(dict(id=article['slug'],text=text['title']+'. '+text['summary'],terms=title*2+summary,title_terms=title,phrases=phrases))
    vectors=tfidf([record['terms'] for record in records])
    semantic=embedding_vectors([record['text'] for record in records])
    distances=[[max(0.0,min(2.0,1-sum(x*y for x,y in zip(a,b)))) if i!=j else 0.0 for j,b in enumerate(semantic)] for i,a in enumerate(semantic)]
    groups,scores=partition(distances)
    groups=sorted(groups,key=lambda group:(-len(group),min(group)))
    clusters=[];items=[]
    for number,group in enumerate(groups,1):
        terms={word for i in group for word in records[i]['title_terms']}
        def contrast(values):
            score=Counter()
            for i,vector in enumerate(values):
                coefficient=1/len(group) if i in group else -1/(len(records)-len(group))
                for term,value in vector.items():score[term]+=coefficient*value
            return score
        keywords=[word for word,_ in sorted(contrast(vectors).items(),key=lambda pair:(-pair[1],pair[0])) if word in terms][:3]
        frequency=Counter(phrase for i in group for phrase in set(records[i]['phrases']))
        candidates=sorted(frequency)
        center=[sum(semantic[i][j] for i in group)/len(group) for j in range(len(semantic[0]))]
        norm=sqrt(sum(value*value for value in center)) or 1
        center=[value/norm for value in center]
        phrase_vectors=embedding_vectors(candidates)
        label=max(zip(candidates,phrase_vectors),key=lambda pair:(sum(a*b for a,b in zip(center,pair[1])),pair[0]))[0] if candidates else (keywords[0] if keywords else '')
        label=surfaces[label].most_common(1)[0][0] if label else 'Articles'
        label=label[0].upper()+label[1:]
        members=[records[i]['id'] for i in sorted(group)]
        clusters.append(dict(id=number,slug=f'cluster-{number}',label=label,keywords=keywords,
                             href=f'topics/cluster-{number}.html',articles=members,
                             description='Articles grouped automatically by similarities in their titles and summaries.'))
        for i in sorted(group):
            record=records[i];link=links[record['id']]
            items.append(dict(id=record['id'],title=link['title'],href=link['href'],lang=link['lang'],cluster=number))
    return dict(schema_version=2,corpus_sha256=sha256(json.dumps(records,sort_keys=True).encode()).hexdigest(),
                method=dict(features='L2-normalized sentence embeddings of English titles and summaries',model=MODEL,model_revision=REVISION,dimensions=384,
                            clustering='agglomerative clustering',linkage='average',distance='cosine',
                            selection='highest mean silhouette over k=2..min(10,n-1); ties favor fewer groups; nonpositive scores give one group',
                            labels='existing member-title phrase closest to the mean sentence-embedding direction; fallback to distinctive title term'),
                article_count=len(records),cluster_count=len(clusters),candidate_scores=scores,clusters=clusters,articles=items)
