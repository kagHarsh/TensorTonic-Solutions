import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Return the mean multiclass cross-entropy loss.
    """
    # Write code here
    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=float)
    row_indices = np.arange(len(y_true))
    print(row_indices)
    correct_prob = y_pred[row_indices, y_true]
    return float(-np.mean(np.log(correct_prob)))