import numpy as np
from optimization.ga.fitness import fitness
from config.config import CONFIG
from optics.aerial_image import compute_aerial_image


def selection(
    potential_parents: np.ndarray,
    target_pattern: np.ndarray
) -> np.ndarray:

    # Retrieve the number of parents to retain for crossover.
    crossover_parent_count = CONFIG["optimization"]["crossover_parent_count"]

    # Store each individual's fitness score and corresponding mask.
    parent_data = []

    # Evaluate every individual in the current population.
    for individual in potential_parents:

        # Calculate the aerial image produced by the candidate mask.
        candidate_aerial_image = compute_aerial_image(individual)

        # Evaluate the candidate against the desired geometric pattern.
        score = fitness(
            target_pattern,
            candidate_aerial_image
        )

        # Store the fitness score and candidate mask together.
        parent_data.append((score, individual))

    # Sort candidates by fitness, with the lowest error first.
    parent_data.sort(key=lambda x: x[0])

    # Retain the highest-performing individuals.
    selected = [
        item[1] for item in parent_data[:crossover_parent_count]
    ]

    # Return the selected parent masks as a NumPy array.
    return np.array(selected)
