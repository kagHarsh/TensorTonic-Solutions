import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len:
        L = max_len
    else:
        L = max(len(seq) for seq in seqs)
    N = len(seqs)
    result = []

    for seq in seqs:
        D = len(seq)
        if D >= L:
            result.append(list(seq[:L]))
        else:
            result.append(list(seq) + [pad_value] * (L-D))
        

    return np.array(result, dtype=float)

    