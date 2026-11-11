"""
=================================================================================
AI ASSISTANCE DISCLOSURE - visualization/progress_plotter.py
=================================================================================
This file was created with AI assistance. It provides a scaffold for plotting 
optimization progress (fitness error vs generation) during GA/SAGA evolution.

Student verification required:
1. Read docstring explaining fitness tracking requirements
2. Implement plotting of best individual fitness per generation  
3. Verify plot has proper title, axis labels, legend, grid
4. Test saving figure to file with specified DPI and format

Date created: 2026-11-11
=================================================================================
"""

import matplotlib.pyplot as plt


# ================================================================================
# FUNCTION: plot_optimization_progress
# ================================================================================

def plot_optimization_progress(ga_history, saga_history=None):
    """
    Plot optimization progress showing fitness error vs generation.
    
    TODO-progress-plotting-code:
      
      Student to implement visualization function using matplotlib
      
      Expected output characteristics:
        - Line plot of best fitness (error) vs generation number  
        - Optional overlay of SAGA results for comparison
        - X-axis labeled "Generation", y-axis labeled "Fitness Error" or "IoU"
        - Title like "Optimization Progress: GA and SAGA Comparison"
        
      Plot elements to include:
        - Fitness line for GA (red or blue marker)
        - Fitness line for SAGA (green or orange marker, optional)
        - Legend identifying each curve
        - Grid enabled for readability
        
      Save options supported:
        - Figure size from config parameters  
        - DPI setting for output quality
        - Format: PNG, PDF, SVG as needed
    
    TODO-progress-plotting-axis-limits-code: 
      
      Set appropriate axis limits based on data range:
        - X-axis auto-scales to fit generation count (0 to max)
        - Y-axis set to include full fitness error range
        
      Optionally add horizontal line at target IoU threshold for visual reference.
    
    TODO-progress-plotting-save-figure-code: 
      
      Implement figure saving logic:
        fig.savefig('optimization_progress.png', dpi=fig_params['save_dpi'])
        
      Also return fig object for further modifications if needed.
      
    Parameters:
      ga_history: List of tuples (generation, best_fitness) from GA optimization
      saga_history: Optional list of same format from SAGA comparison
      
    Returns:
      matplotlib.figure.Figure: Figure object for display or saving
      
    Implementation after TODO marker below...
    """
    
    pass  # Student implementation here
