import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    if x.ndim == 1:
        power = x - np.max(x)
        exp_val = np.exp(power)
        return exp_val/np.sum(exp_val)

    power = x - np.max(x, axis=1, keepdims=True)
    exp_val = np.exp(power)
    return exp_val/np.sum(exp_val, axis=1, keepdims=True)