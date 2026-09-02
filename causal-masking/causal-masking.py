import numpy as np

def apply_causal_mask(scores: list, mask_value: float = -1e9) -> np.ndarray:
    """
    Returns a causally masked NumPy array matching the shape of scores.
    """
    # Write code here
    np.asarray(scores, dtype=float)
    n = scores.shape[-1]
    future = np.triu(
        np.ones((n, n), dtype=bool),
        k=1,
    )
    masked = scores.copy()
    masked[..., future] = mask_value
    return masked