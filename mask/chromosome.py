"""
=================================================================================
AI ASSISTANCE DISCLOSURE - mask/chromosome.py
=================================================================================
This file was created with AI assistance. It provides a scaffold for the 
MaskFeature class used to represent individual GA chromosomes (mask configurations).

Student verification required:
1. Read docstring explaining chromosome data model and attributes
2. Implement __init__ method to initialize feature storage
3. Implement add_feature() method to add rectangular OPC features
4. Implement remove_feature() method to delete features by index
5. Test with known sequences of operations
6. Verify vertex ordering is consistent

Date created: 2026-11-11
=================================================================================
"""

import numpy as np
from typing import List, Tuple


# ================================================================================
# CLASS: MaskFeature
# ================================================================================

class MaskFeature:
    """
    Represents a single optimized photomask configuration for GA population.
    
    Data model explanation:
      Each MaskFeature instance stores a list of rectangular polygons that
      together form the mask pattern to be evaluated. The mask is composed
      of multiple rectangle features added/removed during GA optimization.
      
      Attributes stored after initialization:
        - _vertices: list of (x, y) coordinate tuples for all feature vertices
        - _feature_types: list of "rectangle" type strings for each polygon
        - _grid_resolution: pixels per micron resolution from config
        - _window_bounds: simulation grid boundary in microns
        
    Physical interpretation:
      Each rectangle represents an OPC correction or original design element.
      Vertices stored in counter-clockwise (CCW) winding order starting 
      from bottom-left corner for consistency with optical modeling convention.
      
    TODO-chromosome-initialization: 
      Implement __init__ method to:
      
      Parameters for initialization:
        shape: tuple of grid dimensions (width_px, height_px) or physical size in µm
        grid_resolution: pixels per micron resolution (default from config)
        
      Internal storage decisions:
        - Store all vertices as list of (x, y) tuples in microns
        - Track feature types (currently only "rectangle")
        - Track bounding box for efficiency
        
    Expected after init():
      _vertices = []           # Will contain all vertex coordinates
      _feature_types = []      # Feature type strings
      _n_features = 0          # Number of features stored
      
    TODO-chromosome-initialization-code:
      
    def __init__(self, shape, grid_resolution=5.0):
        """Initialize empty mask chromosome."""
        self._vertices = []
        self._feature_types = []
        self._grid_resolution = grid_resolution
        # Additional attributes as needed
        
    TODO-chromosome-add-feature-implementation:
      
    def add_feature(self, x_center_um, y_center_um, width_um, height_um):
        """
        Add a rectangular OPC feature to the mask.
        
        Physical model:
          Rectangle centered at (x_center, y_center) with given dimensions.
          This represents either an original design element or OPC correction.
          
        TODO: 
          1. Validate input parameters (non-negative sizes, reasonable bounds)
          2. Compute vertex coordinates from center and dimensions
          3. Store vertices in CCW order starting bottom-left corner  
          4. Append to internal vertex and type lists
        
        After adding rectangle at center (cx, cy) with width w and height h:
          x_min = cx - w/2
          x_max = cx + w/2  
          y_min = cy - h/2
          y_max = cy + h/2
          
          Vertices in CCW order from bottom-left:
          [(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)]
          
        TODO-chromosome-remove-feature-implementation:
      
    def remove_feature(self, index):
        """Remove feature at given index from internal storage."""
        pass  # Student to implement
        
    TODO-chromosome-get-methods:
      Implement getter methods for external access:
      - get_vertices(): return all vertex coordinates
      - get_n_features(): return number of stored features
      - get_feature_area(): compute total opaque area in µm²
      
    Raises:
        ValueError: If feature dimensions invalid or out of bounds  
        IndexError: If remove_feature called with invalid index
    
    Implementation after TODO markers below...
    """
    
    def __init__(self, shape, grid_resolution=5.0):
        # TODO-chromosome-initialization-code
        
        pass  # Student implementation here
    
    def add_feature(self, x_center_um, y_center_um, width_um, height_um) -> bool:
        # TODO-chromosome-add-feature-implementation
        
        pass  # Student implementation here
    
    def remove_feature(self, index: int) -> bool:
        # TODO-chromosome-remove-feature-implementation
        
        pass  # Student implementation here
