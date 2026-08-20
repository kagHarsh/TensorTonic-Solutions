import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x, float)
    rng = rng if isinstance(rng, np.random.Generator) else np.random.default_rng(0)
    print("rng --> ", rng)
    keep = 1.0 - p
    print("keep -->", keep)
    mask = (rng.random(x.shape) < keep).astype(float) / keep
    print("mask --> ", mask)
    return x*mask, mask