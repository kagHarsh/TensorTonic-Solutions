def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Return the micro-averaged F1 score rounded to four decimals.
    """
    # Write code here
    true_positive = sum(
        actual == predicted
        for actual, predicted in zip(y_true, y_pred)
    )
    print(true_positive)
    errors = len(y_true) - true_positive
    denominator = 2*true_positive + 2*errors
    return round(2*true_positive/denominator, 4)