import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import topic_embeddings as encoder


class EmbeddingCacheTests(unittest.TestCase):
    def test_cache_is_keyed_by_text_and_pinned_model(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(encoder,'BASE',Path(folder)), patch.object(encoder,'infer',return_value=[[1.0]+[0.0]*383]) as infer:
            first=encoder.embedding_vectors(['First text'])
            self.assertEqual(encoder.embedding_vectors(['First text']),first)
            self.assertEqual(infer.call_count,1)
            encoder.embedding_vectors(['Changed text'])
            self.assertEqual(infer.call_count,2)
            path=Path(folder)/'topic-embeddings.json';cache=json.loads(path.read_text())
            cache['revision']='wrong';path.write_text(json.dumps(cache))
            with self.assertRaisesRegex(ValueError,'pinned model'):encoder.embedding_vectors(['First text'])
