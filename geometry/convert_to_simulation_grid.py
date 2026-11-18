"""
=================================================================================
AI ASSISTANCE DISCLOSURE - geometry/convert_to_simulation_grid.py
=================================================================================
This file was created with AI assistance. It provides a scaffold for converting 
geometric polygons to simulation grid representation (rasterization).

Student verification required:
1. Read docstring explaining physical meaning of px_per_um parameter
2. Implement polygon-to-grid rasterization algorithm
3. Test with simple rectangular features and verify pixel coverage
4. Verify output grid matches expected dimensions

Date created: 2026-11-11
Student tasks marked with TODO-grid-rasterization and [STUDENT-VERIFY] notes
=================================================================================
"""

import numpy as np
from typing import List, Tuple
from shapely import Polygon as GeometryPolygon
from geometry.export_mask_as_polygons import export_mask_as_polygons
from config.config import CONFIG
from shapely.geometry import Point

# ================================================================================
# FUNCTION: convert_to_simulation_grid
# ================================================================================

def convert_to_simulation_grid(
    polygons: List[Tuple[np.ndarray, str]], 
    grid_resolution_px_per_um: float = CONFIG["optics"]["grid_resolution_px_per_um"],
) -> np.ndarray:
    """
    Convert geometric polygons to simulation grid representation.
    
    Physical model explanation:
      This function maps continuous polygon features onto a discrete numerical 
      grid for FFT-based optical simulation. Each grid cell represents a physical 
      area of (1/px_per_um) microns on each side.
      
      Grid coordinate system convention:
        - Origin at bottom-left corner of simulation window
        - X axis increases to the right (standard image coordinates)
        - Y axis increases upward (consistent with optical physics convention)
          
    Physical interpretation of parameters:
      polygons: List of polygon vertex arrays from import_gds or export_mask_as_polygons
      grid_resolution_px_per_um: Pixels per micron resolution, controls discretization
      
      With px_per_um = 200.0:
        - Each pixel represents a physical area of (1/40) = 0.005 µm × 0.005 µm
        - A feature of width 1µm spans 200 pixels in grid representation
        - This matches your specified 5nm/pixel resolution target
      
    Rasterization algorithm:
      1. Determine simulation window bounds from polygon features (or use fixed size)
      2. Compute grid dimensions needed to cover bounding box
      3. Initialize empty float array of shape (height_px, width_px)
      4. For each polygon, determine which grid cells it covers
         - Sample polygon edges at grid resolution or use polygon clipping
         - Mark covered cells as opaque (1.0) or transparent (0.0)
      5. Return rasterized transmission mask array
      
    TODO-grid-rasterization: 
      Implement polygon-to-grid rasterization logic
      
      Implementation options:
      Option A: Sample-based approach (simpler but less accurate)
        - For each polygon, determine bounding box in grid coordinates
        - Iterate over all pixels within that bounding box
        - Test if pixel center lies inside polygon (point-in-polygon test)
        - Mark as opaque or transparent based on result
      
      Option B: Sutherland-Hodgman clipping (more accurate but complex)
        - Clip polygon against grid cell boundaries
        - Use for precise coverage of partial pixels
      
      Option C: Grid sampling at polygon vertices
        - Sample polygon edges at grid resolution
        - Fill between sampled points
      
      For initial OPC optimization, Option A provides sufficient accuracy.
      
    [STUDENT-VERIFY]: 
      Test with known rectangular features:
      - Create simple 2x2 micron rectangle centered at (5, 5)
      - Rasterize and verify exactly 200x200 pixels marked as opaque
      - Check that surrounding pixels remain transparent
      
    Parameters:
      polygons (List[Tuple[np.ndarray, str]]): Input geometric features from previous modules
        Each tuple contains (vertices_array, feature_type)
      grid_resolution_px_per_um (float, default=200.0): Pixels per micron resolution
      
    Returns:
      np.ndarray: 2D float/bool array representing mask transmission
        shape: (height_px, width_px) in grid pixels
        values: 0.0 (transparent/background), 1.0 (opaque feature)
      
    Expected output characteristics:
      - dtype can be float32 or bool depending on implementation choice
      - Values in {0.0, 1.0} for binary mask (or normalized transmission)
      - Shape matches simulation grid dimensions
      
    TODO-grid-rasterization-implementation-hints: 
      After implementing algorithm, consider these edge cases:
      
      1. Grid origin and window bounds:
         - Determine where simulation grid starts (x=0, y=0 in design coordinates?)
         - Or add fixed offset margin around feature centers
      
      2. Partial coverage near grid boundaries:
         - Features outside visible area should be clipped to grid
      
      3. Multiple overlapping polygons:
         - Union operation ensures combined opaque regions marked
         - Use np.maximum for simple binary mask (OR operation)
      
      Example implementation sketch using point-in-polygon test:
        # After importing necessary functions:
        from shapely import Polygon as GeometryPolygon
        
        grid_origin_x = 0.0  # or some offset in microns
        grid_origin_y = 0.0
        
        # For each polygon, compute grid cell indices:
        min_x_um, max_x_um = polygon_minmax(vertices[:, 0])
        min_y_um, max_y_um = polygon_minmax(vertices[:, 1])
        
        start_col_idx = int((grid_origin_x - min_x_um) * px_per_um)
        end_col_idx = int((min(max_x_um, window_max_x) - grid_origin_x) * px_per_um)
        # ... similar for y dimension
        
        for col in range(start_col_idx, end_col_idx):
            for row in range(start_row_idx, end_row_idx):
                pixel_center_x = grid_origin_x + (col + 0.5) / px_per_um
                pixel_center_y = grid_origin_y + (row + 0.5) / px_per_um
                
                # Test if pixel center inside polygon
                if GeometryPolygon(vertices).contains(
                    point=(pixel_center_x, pixel_center_y)):
                    output_grid[row, col] = 1.0

    Raises:
      ValueError: If grid_resolution_px_per_um is non-positive or too large
      ValueError: If polygons list is empty
      TypeError: If polygons contains invalid objects
    
    Implementation begins after TODO marker below...
    """
    # TODO-grid-rasterization-student-implementation-start
    
    # Import shapely for polygon operations (or implement manually)
    # from shapely import Polygon, Point, box  # or use numpy-only approach
    
    # Compute grid dimensions based on feature extents or use fixed size
    # TODO: Add logic to determine appropriate grid size
    
    # Initialize output grid array
    # output_grid = np.zeros((grid_height, grid_width), dtype=np.float32)
    
    # TODO: Implement rasterization loop over polygons
    #       For each polygon, fill covered grid cells
    
    
    # Student implementation skeleton:
    
    # reading in window size through YAML
    WINDOW_SIZE = CONFIG["optics"]["window_size_xy"]
    windowx, windowy = WINDOW_SIZE, WINDOW_SIZE
    
    output_grid = np.zeros((windowx, windowy), dtype=np.float32)
    
    grid_origin_x = 0
    grid_origin_y = 0
    
    
    # HELPED BY QWEN 3.5: polygon_minmax not importing correctly: temp fix(look into polygon_minmax function)
    all_x_coords = []
    all_y_coords = []

    for vertices_data in polygons:
        vertices = vertices_data[0]
        if not isinstance(vertices, np.ndarray):
            vertices = np.array(vertices)
          
        if len(vertices.shape) == 1 and len(vertices) > 0:
            vertices = vertices.reshape(-1, 2)

        if vertices.size > 0:
            all_x_coords.extend(vertices[:, 0])
            all_y_coords.extend(vertices[:, 1])

    if all_x_coords:
        min_x_um, max_x_um = np.min(all_x_coords), np.max(all_x_coords)
    else:
        min_x_um, max_x_um = 0.0, 0.0
    if all_y_coords:
        min_y_um, max_y_um = np.min(all_y_coords), np.max(all_y_coords)
    else:
        min_y_um, max_y_um = 0.0, 0.0
        
    # end here
        
    start_col_idx = int(np.floor((min_x_um - grid_origin_x) * grid_resolution_px_per_um))
    end_col_idx = min(windowx, int(np.ceil((max_x_um - grid_origin_x) * grid_resolution_px_per_um)))

    start_row_idy = int(np.floor((min_y_um - grid_origin_y) * grid_resolution_px_per_um))
    end_row_idy = min(windowy, int(np.ceil((max_y_um - grid_origin_y) * grid_resolution_px_per_um)))
    
    for col in range(start_col_idx, end_col_idx):
      for row in range(start_row_idy, end_row_idy):
        pixel_center_x = grid_origin_x + (col + 0.5) / grid_resolution_px_per_um
        pixel_center_y = grid_origin_y + (row + 0.5) / grid_resolution_px_per_um
        
        # Helped by Qwen 3.5 to fix polygon only reading x coordinates bug
        # FIXED: Check if ANY polygon contains this pixel center
        for vertices_data in polygons:
            vertices = vertices_data[0]
            
            if len(vertices.shape) == 1 and len(vertices) > 0:
                vertices = vertices.reshape(-1, 2)
                
            try:
              if GeometryPolygon(vertices).contains(Point(pixel_center_x, pixel_center_y)):
                output_grid[row, col] = 1.0
            except (ValueError, TypeError):
              continue
    
    return output_grid