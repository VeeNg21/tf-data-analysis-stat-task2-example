import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1374771107 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    x_mean = x.mean()
    x_std = x.std(ddof=1)
    n = len(x)
    alpha = 1 - p
    t_val = t.ppf(1 - alpha/2, df=n-1)
    
    margin_error = t_val * (x_std / np.sqrt(n))
    ci_low = x_mean - margin_error
    ci_high = x_mean + margin_error
    
    return ci_low, ci_high
