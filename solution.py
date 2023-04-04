import pandas as pd
import numpy as np
from scipy.stats import t
from scipy.stats import norm

chat_id = 1374771107 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    df = n - 1
    alpha = 1 - p
    t_critical = t.ppf(1 - alpha / 2, df)
    x_bar = np.mean(x)
    s = np.std(x, ddof=1)
    margin_of_error = t_critical * s / np.sqrt(n)
    lower_bound = x_bar - margin_of_error
    upper_bound = x_bar + margin_of_error
    return (lower_bound, upper_bound)
