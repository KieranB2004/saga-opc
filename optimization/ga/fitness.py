
import numpy as np
from sklearn.metrics import mean_squared_error
from config.config import CONFIG


def fitness(
    target_pattern: np.ndarray,
    candidate_aerial_image: np.ndarray
) -> float:

    # Convert the candidate aerial image into a binary developed pattern.
    threshold = CONFIG["printing"]["default_intensity_threshold"]
    candidate_pattern = candidate_aerial_image >= threshold

    # Calculate the mean squared error between the desired and developed patterns.
    MSE = mean_squared_error(
        target_pattern.ravel(),
        candidate_pattern.ravel()
    )

    return MSE
