"""Frozen local sentence embeddings; no article text is sent to an API."""
from hashlib import sha256
from pathlib import Path
import json
import urllib.request
from math import isfinite

BASE = Path(__file__).parent
MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
REVISION = '1110a243fdf4706b3f48f1d95db1a4f5529b4d41'
_runtime = None


def text_key(text):
    return sha256(text.encode('utf-8')).hexdigest()


def model_files():
    folder = BASE / '.topic-model' / REVISION
    folder.mkdir(parents=True, exist_ok=True)
    for name in ('tokenizer.json', 'onnx/model.onnx'):
        path = folder / name
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            url = f'https://huggingface.co/{MODEL}/resolve/{REVISION}/{name}'
            with urllib.request.urlopen(url, timeout=120) as response:
                data = response.read()
            path.write_bytes(data)
    return folder


def infer(texts):
    global _runtime
    import numpy as np
    import onnxruntime as ort
    from tokenizers import Tokenizer
    if _runtime is None:
        folder = model_files()
        tokenizer = Tokenizer.from_file(str(folder / 'tokenizer.json'))
        tokenizer.enable_truncation(max_length=256)
        tokenizer.enable_padding(pad_id=0, pad_token='[PAD]')
        options = ort.SessionOptions()
        options.intra_op_num_threads = 2
        session = ort.InferenceSession(str(folder / 'onnx/model.onnx'), sess_options=options, providers=['CPUExecutionProvider'])
        _runtime = tokenizer, session
    tokenizer, session = _runtime
    vectors = []
    for start in range(0, len(texts), 16):
        encoded = tokenizer.encode_batch(texts[start:start+16])
        arrays = {name: np.array([getattr(item, attr) for item in encoded], dtype=np.int64)
                  for name, attr in [('input_ids', 'ids'), ('attention_mask', 'attention_mask'), ('token_type_ids', 'type_ids')]}
        hidden = session.run(None, {item.name: arrays[item.name] for item in session.get_inputs()})[0]
        mask = arrays['attention_mask'][..., None]
        pooled = (hidden * mask).sum(axis=1) / np.maximum(mask.sum(axis=1), 1)
        pooled /= np.maximum(np.linalg.norm(pooled, axis=1, keepdims=True), 1e-12)
        vectors.extend([[round(float(value), 8) for value in row] for row in pooled])
    return vectors


def embedding_vectors(texts):
    path = BASE / 'topic-embeddings.json'
    cache = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'model': MODEL, 'revision': REVISION, 'vectors': {}}
    if cache['model'] != MODEL or cache['revision'] != REVISION:
        raise ValueError('Sentence embedding cache does not match the pinned model')
    missing = list(dict.fromkeys(text for text in texts if text_key(text) not in cache['vectors']))
    if missing:
        for text, vector in zip(missing, infer(missing), strict=True):
            cache['vectors'][text_key(text)] = vector
        path.write_text(json.dumps(cache, separators=(',', ':')) + '\n', encoding='utf-8')
    result = [cache['vectors'][text_key(text)] for text in texts]
    if any(len(vector) != 384 or not all(isfinite(value) for value in vector) for vector in result):
        raise ValueError('Invalid sentence embedding vector')
    return result


if __name__ == '__main__':
    model_files()
