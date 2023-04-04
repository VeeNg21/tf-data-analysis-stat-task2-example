import pandas as pd
import numpy as np

from scipy.stats import laplace
from scipy.stats import norm

chat_id = 1374771107 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.ndarray) -> tuple:
    alpha = 1 - p
    n = len(x)
    b = np.sqrt(2*np.log(2/alpha)) / np.sqrt(n)
    loc = np.median(x)
    return loc - b, loc + b
