from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Retriever:

    def __init__(self):

        self.vectorizer = TfidfVectorizer()

        self.chunk_vectors = None

        self.chunks = []

        self.sources = []

    def build_index(self, chunks, sources):

        self.chunks = chunks

        self.sources = sources

        self.chunk_vectors = self.vectorizer.fit_transform(chunks)

    def retrieve(self, query, top_k=3):

        if not self.chunks:
            return []

        query_vector = self.vectorizer.transform([query])

        similarities = cosine_similarity(
            query_vector,
            self.chunk_vectors
        )[0]

        ranked_indices = similarities.argsort()[::-1]

        results = []

        for idx in ranked_indices[:top_k]:

            results.append(
                {
                    "chunk": self.chunks[idx],
                    "source": self.sources[idx],
                    "score": float(similarities[idx])
                }
            )

        return results