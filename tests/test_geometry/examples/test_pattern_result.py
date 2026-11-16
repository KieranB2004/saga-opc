"""
=================================================================================
AI ASSISTANCE DISCLOSURE - tests/test_geometry/examples/test_pattern_result.py
=================================================================================
This file was created with assistance from Qwen 3.5 via OpenCode tooling for 
testing GDS import, grid conversion, and visualization workflows in the SAGA-OPC 
project.

Verification tasks completed by the student engineer:
1. Reviewed and understood the docstring explaining rasterization parameters and pixel resolution
2. Fixed config/parameters.yaml YAML syntax errors
3. Implemented centered bounding-box rasterization for rectangular test features
4. Created matplotlib visualization with x,y pixel coordinate axes showing micron conversion rates
5. Verified that the optical simulation uses {PX_PER_UM} px/µm resolution ({1/PX_PER_UM:.3f} µm/pixel)

Date created/verified: 2026-11-15
=================================================================================
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np
import matplotlib.pyplot as plt
from shapely import Polygon
from config.config import CONFIG
import matplotlib.cm as cm
from matplotlib.colors import TwoSlopeNorm, Normalize, LinearSegmentedColormap

PX_PER_UM = CONFIG["optics"]["grid_resolution_px_per_um"]
WINDOW_SIZE = CONFIG["optics"]["window_size_xy"]

test_rectangle1 = np.array([(10.0, 10.0), (16.0, 10.0), (16.0, 12.0), (10.0, 12.0)])
polygons = [test_rectangle1]
all_vertices = np.vstack(polygons) 

output_grid = np.zeros((WINDOW_SIZE, WINDOW_SIZE), dtype=np.float32)

x_min, x_max = all_vertices[:, 0].min(), all_vertices[:, 0].max()
y_min, y_max = all_vertices[:, 1].min(), all_vertices[:, 1].max()

# Calculate feature size in pixels
feature_width_px = (x_max - x_min) * PX_PER_UM
feature_height_px = (y_max - y_min) * PX_PER_UM

# Use centered placement within the large grid to show feature clearly
CENTER_X = WINDOW_SIZE // 2
CENTER_Y = WINDOW_SIZE // 2    

# Calculate pixel row/column indices for centered feature placement
col_start = CENTER_X - int(feature_width_px / 2)
col_end = CENTER_X + int(feature_width_px / 2)
row_start = CENTER_Y - int(feature_height_px / 2)
row_end = CENTER_Y + int(feature_height_px / 2)

print(f"Feature placed at: rows {row_start}-{row_end}, cols {col_start}-{col_end}")

# Fill the grid with opaque values for feature pixels
output_grid[row_start:row_end, col_start:col_end] = 1.0

num_opaque_pixels = np.sum(output_grid)
print(f"Total opaque pixels (feature area): {num_opaque_pixels:.1f} pixels²")

# Create figure and axis for display
fig, ax = plt.subplots(figsize=(8, 6))

# Display the mask grid as an image
im = ax.imshow(output_grid, cmap='binary', vmin=0, vmax=1)

# Set x-axis label showing both units
ax.set_xlabel(f'X (pixels) / ({1/PX_PER_UM:.3f} µm per pixel)')

# Set y-axis label showing both units
ax.set_ylabel(f'Y (pixels) / ({1/PX_PER_UM:.3f} µm per pixel)')

# Add title describing what this shows
ax.set_title('Rasterized Mask Visualization\nOpaque regions = mask features, Transparent = background')

# Add a colorbar showing intensity/transmission
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Transmission (0.0 = transparent, 1.0 = opaque)')

# Set axis ticks for readability (every 256 pixels)
step = 256
ax.set_xticks(range(0, WINDOW_SIZE, step))
ax.set_yticks(range(0, WINDOW_SIZE, step))

# Print feature pixel location info
print(f"\nFeature displayed at pixel coordinates: rows {row_start}-{row_end}, cols {col_start}-{col_end}")

# Save figure to file

save_path = 'tests/test_geometry/examples/mask_visualization.png'
plt.savefig(save_path, dpi=300)
print(f"✓ Mask visualization saved to: {save_path}")

# Show the figure
plt.tight_layout()
plt.show()

print("\nTest pattern rendering complete!")
print(f"  - Feature centered in grid")
print(f"  - X and Y axes show pixel coordinates")
print(f"  - Resolution: {PX_PER_UM} pixels per micron ({1/PX_PER_UM:.3f} µm/pixel)")