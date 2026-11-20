from sklearn.metrics import mean_squared_error
import numpy as np

def fitness(parentchromosome: np.ndarray, mask: np.ndarray) -> float:
    MSE = mean_squared_error(mask, parentchromosome)
    return MSE