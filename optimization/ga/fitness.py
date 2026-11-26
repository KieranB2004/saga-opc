import numpy as np

def fitness(
    target_pattern: np.ndarray,
    candidate_aerial_image: np.ndarray
) -> float:

    target_pattern = np.asarray(target_pattern, dtype = float)
    candidate_aerial_image = np.asarray(candidate_aerial_image, dtype = float)

    MSE = np.mean((target_pattern - candidate_aerial_image) ** 2)

    return float(MSE)