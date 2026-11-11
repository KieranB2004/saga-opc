"""
=================================================================================
AI ASSISTANCE DISCLOSURE - geometry/export_mask_as_polygons.py
=================================================================================
This file was created with AI assistance. It provides a scaffold for converting 
optimized mask representations (stored as dictionaries) into polygon coordinate lists.

Student verification required:
1. Read docstring explaining input data structure
2. Implement conversion from dictionary feature specs to polygon vertices
3. Ensure correct vertex ordering (consistent clockwise or counter-clockwise)
4. Handle edge cases: empty feature list, malformed coordinates
5. Test with known output and compare against expected results

Date created: 2026-11-11
Student tasks marked with TODO-export-mask-conversion and [STUDENT-VERIFY] notes
=================================================================================
"""

import numpy as np
from typing import List, Dict


# ================================================================================
# FUNCTION: export_mask_as_polygons
# ================================================================================

def export_mask_as_polygons(mask_data: Dict) -> List[Tuple[np.ndarray, str]]:
    """
    Convert optimized mask representation to polygon coordinates.
    
    Physical model explanation:
      After GA/SAGA optimization, the current mask state is stored as a 
      dictionary containing feature types (rectangles for simplified OPC), 
      positions, and dimensions. This function converts that internal 
      representation into standard Polygon objects with explicit vertex coordinates.
      
    Input data structure (dict) example:
      {
        "features": [
          {"type": "rectangle", "x_center": 0.0, "y_center": 5.0, 
           "width": 2.0, "height": 2.0},
          {"type": "rectangle", "x_center": 3.0, "y_center": 8.0,
           "width": 1.5, "height": 1.5},
        ]
      }
      
    Physical interpretation of parameters:
      - x_center, y_center: Feature center coordinates in microns (or grid pixels)
      - width, height: Feature dimensions in same units as coordinate system
      - type: Currently only "rectangle" implemented; may extend to other shapes
      
    TODO-export-mask-conversion: 
      Implement conversion from dict feature specs to polygon vertices
      
      Algorithm steps to implement:
      1. Iterate through feature list in mask_data["features"]
      2. For each rectangle, compute corner coordinates from center and dimensions
      3. Generate vertex list in consistent order (CCW or CW)
      4. Return as list of (vertices_array, type_string) tuples
      
      Vertex ordering convention:
        - Use counter-clockwise (CCW) winding for consistency
        - This matters for normal vectors and surface operations later
        
    [STUDENT-VERIFY]: Verify output vertex order matches expected CCW winding.
                     Test with known rectangle dimensions and compare vertices.
                     
    Parameters:
      mask_data (dict): Dictionary containing optimized mask state
      
    Returns:
      List of tuples: [(vertices_array, feature_type), ...]
        - vertices_array: np.ndarray of shape (4, 2) for each rectangle
                          [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
                          ordered counter-clockwise from bottom-left corner
        - feature_type: String "rectangle" or extended types if added
      
    Expected output structure example:
      [
        (np.array([[0.0, 5.0], [2.0, 5.0], [2.0, 7.0], [0.0, 7.0]]), 
         "rectangle"),
        (np.array([[3.0, 1.0], [4.5, 1.0], [4.5, 2.5], [3.0, 2.5]]), 
         "rectangle"),
      ]
      
    Raises:
      ValueError: If feature dict missing required keys (x, y, width, height)
      TypeError: If features list contains invalid objects
    
    TODO-export-mask-conversion-error-handling: Add validation and error messages
          for malformed input dictionaries.
          
    Implementation hints after TODO marker:
      - Extract "features" list from mask_data dictionary
      - For each feature, access keys: x_center (or x), y_center (or y), 
            width (or w), height (or h)  
      - Compute corners: (x-w/2, y-h/2) to (x+w/2, y+h/2) for bottom-left start
      - Order vertices CCW: bottom-left, bottom-right, top-right, top-left
      """
    # TODO-export-mask-student-implementation-start
    
    # Student implementation skeleton:
    
    # Initialize empty list to collect polygon results
    polygons = []
    
    # TODO: Extract features from mask_data dictionary
    # if "features" in mask_data:
    #     feature_list = mask_data["features"]
    # else:
    #     raise ValueError("mask_data must contain 'features' key")
    
    # Student to implement the conversion logic here
    raise NotImplementedError(
        "Student must implement dictionary-to-polygon conversion logic. "
        "See docstring for required steps and vertex ordering convention."
    )
