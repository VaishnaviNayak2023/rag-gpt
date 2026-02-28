import faiss
import numpy as np
import os
import pickle
from app.core.config import settings

INDEX_PATH = "data/faiss.index"
META_PATH = "data/meta.pkl"

class FAISSStore:

    def __init__(self):
        if os.path.exists(INDEX_PATH):
            self.index = faiss.read_index(INDEX_PATH)
            with open(META_PATH, "rb") as f:
                self.metadata = pickle.load(f)
        else:
            self.index = faiss.IndexFlatL2(settings.VECTOR_DIM)
            self.metadata = []

    def add(self, embeddings, documents):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.metadata.extend(documents)
        faiss.write_index(self.index, INDEX_PATH)

        with open(META_PATH, "wb") as f:
            pickle.dump(self.metadata, f)

    def search(self, embedding, k):
        vector = np.array([embedding]).astype("float32")
        distances, indices = self.index.search(vector, k)

        return [self.metadata[i] for i in indices[0]]
