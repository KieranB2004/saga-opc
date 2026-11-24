
"""
=================================================================================
AI ASSISTANCE DISCLOSURE - optimization/ga/mutation.py  
=================================================================================
This file was created with AI assistance. It provides templates for mutation 
operations that introduce variation into GA chromosome population.

Student verification required:
1. Read docstring explaining mutation purpose in evolutionary algorithms
2. Implement random mutations to mask features (add/remove/modify)
3. Verify mutation preserves population size exactly
4. Test different mutation rates and strength parameters
5. Understand balance between exploration and exploitation

Date created: 2026-11-11
=================================================================================
"""

import numpy as np
from config.config import CONFIG
import numpy as np
from scipy.ndimage import binary_dilation
from config.config import CONFIG
import random
import random

# ================================================================================
# FUNCTION: mutation_apply
# ================================================================================

def mutation_apply(
    population: np.ndarray,
    mutation_rate: float = CONFIG["optimization"]["mutation_rate"],
    margin: int = 5,
    reference_mask: np.ndarray = None
) -> np.ndarray:
    """
    Apply random mutations to maintain/exceed expected population size.
    
    TODO-mutation-operation-logic-code:
      
      Physical interpretation of parameters:
        mutation_rate: Probability that a given feature/location is mutated
          Lower value = less variation introduced (exploitation)
          Higher value = more exploration in search space
        
        NOTE: not used for implementation
        mutation_strength: Magnitude of random perturbation applied
          For position changes: ±strength * current_feature_size  
          For dimension changes: Random offset within [-strength, +strength]
      
      Mutation strategies for OPC mask features:
        
        Strategy 1: Feature addition/removal (binary)
          - Randomly add small rectangle feature to some chromosomes
          - Randomly remove existing features from others
        
        Strategy 2: Feature dimension perturbation
          - Slightly modify width/height of existing rectangles
          - Change position coordinates by random offset
        
        Strategy 3: Grid cell flip (for rasterized representation)
          - Flip value at random grid location (0→1 or 1→0)

          #Engineer NOTE: Strategy 3 shall be implemented
      
    TODO-mutation-verify-size-preservation:
      
      After implementation, verify len(mutated) == expected_n where expected_n
      comes from input parameter or configuration
      
    Parameters:
      population (np.ndarray): Array of individuals
                               shape: (pop_size, *shape_dimensions)
      mutation_rate (float, default=0.1): Probability element is mutated
      margin (int, default=10): Pixels added around the original mask boundaries
      
    Returns:
      np.ndarray: Mutated population with same dimensions as input
    """

    # Convert the input population into a NumPy array.
    population = np.asarray(population)

    # Verify that the population has three dimensions.
    if population.ndim != 3:
        raise ValueError(
            "Population must have dimensions (population, rows, columns)."
        )

    # Verify that the population is not empty.
    if population.shape[0] == 0:
        raise ValueError("Population cannot be empty.")

    # Verify that the population contains spatial dimensions.
    if population.shape[1] == 0 or population.shape[2] == 0:
        raise ValueError("Population spatial dimensions cannot be empty.")

    # Verify that the mutation rate is within the valid range.
    if not 0.0 <= mutation_rate <= 1.0:
        raise ValueError("Mutation rate must be between 0 and 1.")

    # Verify that the mutation margin is non-negative.
    if not isinstance(margin, (int, np.integer)) or margin < 0:
        raise ValueError("Mutation margin must be a non-negative integer.")

    # Require the original mask to define the mutation region.
    if reference_mask is None:
        raise ValueError("An original reference mask must be provided.")

    # Convert the reference mask into a binary array.
    reference_mask = np.asarray(reference_mask) == 1

    # Verify that the reference mask has matching spatial dimensions.
    if reference_mask.shape != population.shape[1:]:
        raise ValueError(
            "Reference mask dimensions must match population dimensions."
        )

    # Verify that the reference mask contains occupied pixels.
    if not np.any(reference_mask):
        raise ValueError("The reference mask contains no occupied pixels.")

    # Verify that the population contains binary values.
    if not np.all(np.isin(population, [0, 1])):
        raise ValueError("Population must contain only binary values (0 and 1).")

    # Copy the population to preserve the original input.
    population_mutate = population.copy()

    # Create a square neighbourhood around every occupied mask pixel.
    mutation_structure = np.ones(
        (2 * margin + 1, 2 * margin + 1),
        dtype=bool
    )

    # Expand the original mask by the specified mutation margin.
    mutation_allowed = binary_dilation(
        reference_mask,
        structure=mutation_structure
    )

    # Generate independent mutation decisions for every population member.
    mutation_decisions = (
        np.random.random(population.shape) < mutation_rate
    )

    # Restrict mutation decisions to the permitted spatial region.
    mutation_decisions &= mutation_allowed[np.newaxis, :, :]

    # Flip the selected binary pixel values.
    population_mutate[mutation_decisions] = (
        1 - population_mutate[mutation_decisions]
    )

    # Return the mutated population with its original dimensions.
    return population_mutate
