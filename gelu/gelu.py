import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    erf = np.vectorize(math.erf)
    return x*0.5*(1.0 + erf(x/np.sqrt(2.0)))