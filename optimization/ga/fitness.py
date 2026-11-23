from sklearn.metrics import mean_squared_error
import numpy as np

def fitness(parentchromosome_aerial_image: np.ndarray, mask_aerial_image: np.ndarray) -> float:
    MSE = mean_squared_error(mask_aerial_image, parentchromosome_aerial_image)
    return MSE