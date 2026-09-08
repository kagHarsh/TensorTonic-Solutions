import numpy as np

def adagrad_step(w: list, g: list, G: list, lr: float = 0.01, eps: float = 1e-8) -> dict:
    """
    Returns a dictionary with new_w and new_G.
    """
    # Write code here
    w = np.asarray(w, dtype=float)
    g = np.asarray(g, dtype=float)
    G = np.asarray(G, dtype=float)
    new_G = G + (g**2)
    new_W = w - ((lr/(np.sqrt(new_G + eps))) * g)
    return {"new_w": new_W, "new_G": new_G}