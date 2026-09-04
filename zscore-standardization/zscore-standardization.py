import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    mean_val = np.mean(X, axis=axis, keepdims=True)
    std_div = np.std(X, axis=axis, keepdims=True)
    std_div = np.where(std_div > eps, std_div, 1.0)
    return (X-mean_val)/std_div
    