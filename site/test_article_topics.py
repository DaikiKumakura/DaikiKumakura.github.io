from pathlib import Path
import tempfile
import unittest
from article_topics import cluster_articles, main_text, tfidf, words
from unittest.mock import patch

def lexical_embeddings(texts):
    from hashlib import sha256
    from math import sqrt
    out=[]
    for text in texts:
        vector=[0.0]*128
        for word in words(text):vector[int(sha256(word.encode()).hexdigest()[:8],16)%128]+=1
        norm=sqrt(sum(x*x for x in vector)) or 1
        out.append([x/norm for x in vector])
    return out



class ArticleClusteringTests(unittest.TestCase):
    def setUp(self):
        self.embedding_patch=patch('article_topics.embedding_vectors',side_effect=lexical_embeddings)
        self.embedding_patch.start();self.addCleanup(self.embedding_patch.stop)

    def articles(self, root):
        articles=[];links={}
        for slug,text in [('a','receptor occupancy kinase binding'),('b','receptor occupancy kinase binding'),
                          ('c','receptor occupancy kinase binding'),('d','tumor survival censoring hazard'),
                          ('e','tumor survival censoring hazard'),('f','tumor survival censoring hazard')]:
            folder=root/slug;folder.mkdir();(folder/'en.md').write_text(text,encoding='utf-8')
            articles.append(dict(slug=slug,folder=folder,meta=dict(draft=False,source_language='en',locales={'en':{'title':text,'summary':text}})))
            links[slug]=dict(title=text,href=f'writing/{slug}.html',lang='en')
        return articles,links

    def test_content_driven_reproducible_communities(self):
        with tempfile.TemporaryDirectory() as directory:
            articles,links=self.articles(Path(directory))
            result=cluster_articles(articles,links)
            self.assertEqual(result,cluster_articles(list(reversed(articles)),links))
            self.assertEqual({frozenset(g['articles']) for g in result['clusters']},{frozenset('abc'),frozenset('def')})
            self.assertNotIn('edges',result)
            self.assertNotIn('nodes',result)
            articles[0]['meta']['locales']['en']['title']='tumor survival censoring hazard'
            self.assertNotEqual(result['corpus_sha256'],cluster_articles(articles,links)['corpus_sha256'])

    def test_empty_singleton_and_exclusions(self):
        self.assertEqual(cluster_articles([],{})['articles'],[])
        with tempfile.TemporaryDirectory() as directory:
            articles,links=self.articles(Path(directory))
            self.assertEqual(cluster_articles(articles[:1],links)['cluster_count'],1)
        self.assertNotIn('unrelated',main_text('Main\n## 参考文献\nunrelated citation'))
        self.assertNotIn('secretcode',main_text('Main\n```python\nsecretcode\n```'))
