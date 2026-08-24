import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Return the Euclidean distance between x and y.
    """
    # Write code here
    x = np.asarray(x, dtype=int)
    y = np.asarray(y, dtype=int)
    return float(np.sqrt(np.sum((x-y)*(x-y))))