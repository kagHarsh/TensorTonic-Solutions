import math
from collections import Counter
import numpy as np

def tfidf_vectorizer(documents: list[str]) -> dict:
    """
    Returns a dictionary with tfidf_matrix and vocabulary.
    """
    # Write code here
    tokenized = [document.lower().split() for document in documents]
    print("tokenized -->", tokenized)
    vocabulary = sorted({token for tokens in tokenized for token in tokens})
    print("vocabulary -->", vocabulary)
    index = {token: position for position, token in enumerate(vocabulary)}
    print("index -->", index)
    matrix = np.zeros((len(documents), len(vocabulary)), dtype=float)
    document_freq = Counter()
    print("document_freq -->", document_freq)
    for tokens in tokenized:
        document_freq.update(set(tokens))
    print("document_freq -->", document_freq)
    for row, tokens in enumerate(tokenized):
        counts = Counter(tokens)
        print("counts -->", counts)
        for token, count in counts.items():
            tf = count / len(tokens)
            idf = math.log(len(documents) / document_freq[token])
            matrix[row, index[token]] = tf * idf

    return {"tfidf_matrix": matrix, "vocabulary": vocabulary}