from pathlib import Path
import tempfile
import unittest
from article_network import article_network, main_text


class ArticleNetworkTests(unittest.TestCase):
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
            result=article_network(articles,links)
            self.assertEqual(result,article_network(list(reversed(articles)),links))
            self.assertEqual({frozenset(g['articles']) for g in result['clusters']},{frozenset('abc'),frozenset('def')})
            for edge in result['edges']:
                self.assertGreater(edge['weight'],0)
                self.assertTrue({edge['source'],edge['target']}<=set('abc') or {edge['source'],edge['target']}<=set('def'))
            articles[0]['meta']['locales']['en']['title']='tumor survival censoring hazard'
            self.assertNotEqual(result['corpus_sha256'],article_network(articles,links)['corpus_sha256'])

    def test_empty_singleton_and_exclusions(self):
        self.assertEqual(article_network([],{})['nodes'],[])
        with tempfile.TemporaryDirectory() as directory:
            articles,links=self.articles(Path(directory))
            self.assertEqual(article_network(articles[:1],links)['edge_count'],0)
        self.assertNotIn('unrelated',main_text('Main\n## 参考文献\nunrelated citation'))
        self.assertNotIn('secretcode',main_text('Main\n```python\nsecretcode\n```'))
