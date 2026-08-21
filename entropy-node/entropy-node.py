import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Return the Shannon entropy of the class labels.
    """
    # Write code here
    y = np.asarray(y, dtype=int)
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    print(counts)
    prob = counts/len(y)
    print(prob)
    ans = -np.sum(prob*np.log2(prob))
    return float(ans)