"""
=================================================================================
AI ASSISTANCE DISCLOSURE - optimization/ga/crossover.py
=================================================================================
This file was created with AI assistance. It provides templates for crossover 
operations in the genetic algorithm for OPC optimization.

Student verification required:
1. Read docstring explaining crossover mathematical formulation
2. Implement selection of top-k parents from population
3. Implement child generation combining parent features appropriately  
4. Verify output has exactly expected_children count
5. Test with varying numbers of parents and children

Date created: 2026-11-11
=================================================================================
"""

import numpy as np
from config.config import CONFIG


# ================================================================================
# FUNCTION: crossover_select
# ================================================================================

def crossover_select(
    parents: np.ndarray, 
    expected_children: int = CONFIG["optimization"]["children_from_crossover"],
) -> np.ndarray:
    """
    Select top-performing parents and generate children via crossover.
    
    TODO-crossover-selection-logic-code:
      
      Student to implement selection and crossover logic
      
      Selection criteria:
        - Rank individuals by fitness score (lower error = better for OPC)
        - Select top N parents where N specified in parent_count parameter
        
      Crossover strategy options for mask features:
        Option 1: Simple feature inheritance
          - Combine features from selected parents
          - Randomly choose each feature from either parent 1 or 2
          
        Option 2: Geometric averaging  
          - Take average position/size of overlapping features from parents
          - Creates intermediate child mask
        
        Option 3: Block crossover for grid patterns
          - Divide chromosome into blocks
          - Alternate block segments from each parent
        
      For simplified OPC with rectangular features, Option 1 is simplest.
      
    Parameters:
      parents (np.ndarray): Array of parent chromosomes
                            shape: (parent_count, *spatial_dimensions)
      expected_children (int, default): Number of children to produce
      
    Returns:
      np.ndarray: Children array with shape (expected_children, *shape)
      
    TODO-crossover-verify-output-count:
      
      After implementation, verify len(children) == expected_children
      
    Raises:
      ValueError: If parents array has wrong dimensions or size
      RuntimeError: If crossover cannot produce requested number of children
    
    Example after implementation complete:
      >>> dummy_parents = np.random.rand(6, 10, 10)
      >>> children = crossover_select(parents=dummy_parents, expected_children=expected_children)
      >>> print(len(children))
    """

    num_parents = parents.shape[0]
    parent_shape = parents.shape[1:]
    
    children = []
    
    for _ in range(expected_children):
        # selecting random parent from list of parents(parent a)
        parent_idx_a = np.random.randint(0, num_parents)
        # selecting random parent from list of parents(parent b)
        parent_idx_b = np.random.randint(0, num_parents)
        # true / false boolean mask for selecting whether parent a or parent b
        mask = np.random.rand(*parent_shape) > 0.5
        # np.where compares boolean mask, if true select parent a, if false select parent b,
        child = np.where(mask, parents[parent_idx_a], parents[parent_idx_b])
        children.append(child)
        
    return np.array(children)
        
    
    
    