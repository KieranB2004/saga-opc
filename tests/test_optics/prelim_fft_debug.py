import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np
import matplotlib.pyplot as plt
from shapely import Polygon
from config.config import CONFIG
import matplotlib.cm as cm
from matplotlib.colors import TwoSlopeNorm, Normalize, LinearSegmentedColormap
from geometry.convert_to_simulation_grid import convert_to_simulation_grid
from optics.aerial_image import compute_aerial_image

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

fft_output_grid = compute_aerial_image(output_grid)

print(fft_output_grid)

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(fft_output_grid, cmap='Blues')
ax.set_xlabel(f'X (pixels) / ({1/PX_PER_UM:.3f} µm per pixel)')
ax.set_ylabel(f'Y (pixels) / ({1/PX_PER_UM:.3f} µm per pixel)')
ax.set_title('fft')
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('frequency')
step = 10
ax.set_xticks(range(0, WINDOW_SIZE, step))
ax.set_yticks(range(0, WINDOW_SIZE, step))
plt.tight_layout()
plt.show()