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
import random

# ================================================================================
# FUNCTION: mutation_apply
# ================================================================================

def mutation_apply(
    population: np.ndarray,  
    mutation_rate: float = CONFIG["optimization"]["mutation_rate"]
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
      population (np.ndarray): Array of individuals to mutate
                               shape: (pop_size, *shape_dimensions)
      mutation_rate (float, default=0.1): Probability element is mutated
      NOTE: not used for implementation
      mutation_strength (float, default=0.05): Magnitude of random perturbation
      
    Returns:
      np.ndarray: Mutated population with same dimensions as input
    
    NOTE: Error handling not done
    TODO-mutation-error-handling-code:
      
      Add error handling for edge cases:
        - mutation_rate outside [0, 1] range
        - Negative mutation_strength  
        - Empty or malformed input array
    
    Example after implementation complete:
      >>> pop_before = np.random.rand(15, 10, 10)
      >>> mutated = mutation_apply(population=pop_before)
      >>> print(len(mutated))  # Should print 15 (same as input)
      
    Implementation after TODO marker below...
    """
    # population is list of current parents + new children
    population_mutate = population.copy()
    
    flat_population_mutate = population_mutate.ravel()
    
    flat_population_mutate_size = len(flat_population_mutate)
    n_flips = int(mutation_rate * flat_population_mutate_size)
    
    if n_flips > 0:
        # selecting random bit positions to flip
        flip_indices = np.random.choice(flat_population_mutate_size, size = n_flips, replace = False)
        
        # flipping bits using NumPy boolean indexing
        population_mutate.flat[flip_indices] = 1 - population_mutate.flat[flip_indices]
    
    return population_mutate
