"""
=================================================================================
AI ASSISTANCE DISCLOSURE - tests/test_geometry/examples/test_pattern_result.py
=================================================================================
This file was created with assistance from Qwen 3.5 via OpenCode tooling for 
testing GDS import, grid conversion, and visualization workflows(matplotlib code done by qwen 3.5) in the SAGA-OPC 
project.

Verification tasks completed by the student engineer:
1. Reviewed and understood the docstring explaining rasterization parameters and pixel resolution
2. Fixed config/parameters.yaml YAML syntax errors
3. Created matplotlib visualization with x,y pixel coordinate axes showing micron conversion rates

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
from geometry.convert_to_simulation_grid import convert_to_simulation_grid

PX_PER_UM = CONFIG["optics"]["grid_resolution_px_per_um"]
WINDOW_SIZE = CONFIG["optics"]["window_size_xy"]


vertices_list1 = [(10.0, 10.0), (16.0, 10.0), (16.0, 12.0), (10.0, 12.0)]
vertices_list2 = [(16.0, 22.0), (18.0, 22.0), (18.0, 10.0), (16.0, 10.0)]
vertices_list3 = [(5.0, 3.0), (13.0, 3.0), (13.0, 5.0), (5.0, 5.0)]
vertices_list4 = [(5.0, 7.0), (13.0, 7.0), (13.0, 9.0), (5.0, 9.0)]
polygons = [
    (np.array(vertices_list1, dtype=float), "opaque"),
    (np.array(vertices_list2, dtype=float), "opaque"),
    (np.array(vertices_list3, dtype=float), "opaque"),
    (np.array(vertices_list4, dtype=float), "opaque")
]

output_grid = convert_to_simulation_grid(
    polygons = polygons,
    grid_resolution_px_per_um = PX_PER_UM
)

### AI GENERATED:

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

### END