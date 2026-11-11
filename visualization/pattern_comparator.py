"""
=================================================================================
AI ASSISTANCE DISCLOSURE - visualization/pattern_comparator.py  
=================================================================================
This file was created with AI assistance. It provides a scaffold for visualizing 
target vs mask vs printed pattern comparison in OPC results.

Student verification required:
1. Read docstring explaining overlay visualization requirements
2. Implement RGB or side-by-side pattern comparison plot
3. Verify all patterns properly aligned and color-coded  
4. Test saving figure with proper labels and legend

Date created: 2026-11-11
=================================================================================
"""

import matplotlib.pyplot as plt


# ================================================================================
# FUNCTION: compare_patterns
# ================================================================================

def compare_patterns(target_grid, mask_grid, print_grid):
    """
    Create side-by-side comparison of target, optimized mask, and printed pattern.
    
    TODO-pattern-comparison-plotting-code:
      
      Student to implement RGB or subplots visualization
      
      Layout options:
        Option 1: Subplots (three panels)
          Left: Target pattern in grayscale or blue
          Center: Optimized mask after OPC in red  
          Right: Predicted printed pattern in green
        
        Option 2: RGB overlay with transparency
          Combine three grids into single image
          Use different RGBA channels for color distinction
      
      Plot characteristics required:
        - Each subplot titled (Target, Mask, Print)
        - Colormap appropriate for each panel (e.g., viridis or grayscale)  
        - Same axis limits across all subplots for alignment
        
      TODO-pattern-comparison-axis-labels-code: 
      
      Add proper labels and units:
        xlabel('X pixels') with conversion to microns if known
        ylabel('Y pixels')  
        colorbar for each subplot showing intensity/value scale
    
    TODO-pattern-comparison-save-figure-code:
      
      Save figure using config DPI settings:
        fig.savefig('pattern_comparison.png', dpi=config['save_dpi'])
        
      Return figure object for further modifications.
    
    Parameters:
      target_grid: Binary 2D array representing desired pattern  
      mask_grid: Optimized mask after GA/SAGA optimization  
      print_grid: Predicted printed resist pattern
      
    Returns:
      matplotlib.figure.Figure: Figure object with subplots or RGB image
    
    Implementation after TODO marker below...
    """
    
    pass  # Student implementation here
