import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    N, D = X.shape
    print("D --> ", D)
    w = np.zeros(D)
    print("W --> ", w)
    b = 0.0
    for _ in range(steps):
        z = X @ w + b #logits
        p = _sigmoid(z) #prediction
        deltaW = X.T @ (p-y) / N
        deltaB = np.mean(p-y)
        w = w - lr*deltaW
        b = b - lr*deltaB

    return w, b