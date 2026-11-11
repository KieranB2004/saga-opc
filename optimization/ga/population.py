"""
=================================================================================
AI ASSISTANCE DISCLOSURE - optimization/ga/population.py
=================================================================================
This file was created with AI assistance. It provides templates for GA 
population management operations (crossover, mutation).

Student verification required:
1. Read docstrings explaining each function's purpose and mathematical basis
2. Implement population initialization creating exactly n_individuals chromosomes  
3. Implement crossover selecting top k parents to produce specified children count
4. Verify mutation operation preserves population size unchanged
5. Test all operations with varying parameter combinations

Date created: 2026-11-11
=================================================================================
"""

import numpy as np
from typing import List, Tuple


# ================================================================================
# FUNCTION: initialize_population
# ================================================================================

def initialize_population(shape: Tuple[int, int], n_individuals: int) -> np.ndarray:
    """
    Initialize GA population with randomly generated mask configurations.
    
    TODO-population-initialization-code:
      
      Student to implement initialization creating exactly n_individuals 
      chromosomes, each with spatial dimensions matching shape parameter.
      
      Physical meaning:
        - Each row represents one complete mask configuration (chromosome)  
        - Columns represent feature data or grid values for that chromosome
        
      Implementation approach options:
        1. Flatten 2D mask pattern into single array per individual
           Initialize with random binary values representing rectangular features
      
      TODO-population-verify-output-shape:
      
      After implementation, verify:
        len(population) == n_individuals
        population[i].shape == shape for all i
    
    Raises:
      ValueError: If n_individuals non-positive or shape dimensions invalid
      TypeError: If parameters wrong type
        
    Parameters:
      shape: Tuple of (width_px, height_px) or grid resolution units
      n_individuals: Number of chromosomes to create
      
    Returns:
      np.ndarray: Array of shape (n_individuals, *shape_flat)
      
    Example usage after implementation:
      >>> pop = initialize_population(shape=(10, 10), n_individuals=15)
      >>> print(f"Population size: {len(pop)}")  # Should print 15
    """
    
    pass  # Student implementation here
