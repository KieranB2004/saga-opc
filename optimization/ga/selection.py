import numpy as np
from optimization.ga.fitness import fitness
from config.config import CONFIG
from optics.aerial_image import compute_aerial_image

# Takes in the parent list, compares its chromosomes to current mask using fitness mean squared error, returns list of top "crossover_parent_count" parents selected
def selection(potential_parents: np.ndarray, mask_aerialimage: np.ndarray) -> np.ndarray:
    
    crossover_parent_count = CONFIG["optimization"]["crossover_parent_count"]
     
    parent_data = []
    for i in range(len(potential_parents)):
        potential_parents_aerial_image = compute_aerial_image(potential_parents[i])
        score = fitness(potential_parents_aerial_image[i], mask_aerialimage)
        parent_data.append((score, potential_parents[i]))
    
    parent_data.sort(key = lambda x: x[0])
    
    selected = [item[1] for item in parent_data[:crossover_parent_count]]
    
    return np.array(selected)
