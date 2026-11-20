import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import time
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

scale_factor = 0.045

start_total = time.perf_counter()

vertices_list1 = [(11.0, 11.5), (17.0, 11.5), (17.0, 13.5), (11.0, 13.5)]
vertices_list2 = [(17.0, 23.0), (19.0, 23.0), (19.0, 11.5), (17.0, 11.5)]
vertices_list3 = [(11.0, 3.5), (19.0, 3.5), (19.0, 5.5), (11.0, 5.5)]
vertices_list4 = [(11.0, 7.5), (19.0, 7.5), (19.0, 9.5), (11.0, 9.5)]
vertices_list5 = [(6.75, 23.0), (9.0, 23.0), (9.0, 3.5), (6.75, 3.5)]
vertices_list6 = [(9.0, 23.0), (15.0, 23.0), (15.0, 21.0), (9.0, 21.0)]
vertices_list7 = [(21.0, 23.0), (23.0, 23.0), (23.0, 3.5), (21.0, 3.5)]

vertices_list1 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list1]
vertices_list2 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list2]
vertices_list3 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list3]
vertices_list4 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list4]
vertices_list5 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list5]
vertices_list6 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list6]
vertices_list7 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list7]

polygons = [
    (np.array(vertices_list1, dtype=float), "opaque"),
    (np.array(vertices_list2, dtype=float), "opaque"),
    (np.array(vertices_list3, dtype=float), "opaque"),
    (np.array(vertices_list4, dtype=float), "opaque"),
    (np.array(vertices_list5, dtype=float), "opaque"),
    (np.array(vertices_list6, dtype=float), "opaque"),
    (np.array(vertices_list7, dtype=float), "opaque")
]

output_grid = convert_to_simulation_grid(
    polygons = polygons,
    grid_resolution_px_per_um = PX_PER_UM
)

fft_output_grid = compute_aerial_image(output_grid)


# THRESHOLD PICKED TO MIMIC EXPECTED RESULTS LIKE OVER FITTING IN THE INSIDE EDGE.
# over fitting in the inside edge happens due to 90 degree turn
threshold = CONFIG["printing"]["default_intensity_threshold"]

developed_mask = fft_output_grid >= threshold

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(developed_mask, cmap='Blues')
ax.set_xlabel(f'X (pixels) / ({1000/PX_PER_UM:.2f} nm per pixel)')
ax.set_ylabel(f'Y (pixels) / ({1000/PX_PER_UM:.2f} nm per pixel)')

# printing desired mask outline
um_to_pixel = 1.0 / PX_PER_UM
for poly_points, _ in polygons:
    pixels = (np.array(poly_points) * PX_PER_UM).tolist()
    poly = Polygon(pixels)
    ax.plot(poly.exterior.xy[0], poly.exterior.xy[1], 'k-', linewidth=4, linestyle='solid')
    
ax.set_title('fft')
step = 16
ax.set_xticks(range(0, WINDOW_SIZE, step))
ax.set_yticks(range(0, WINDOW_SIZE, step))


end_total = time.perf_counter()

print(end_total - start_total)

plt.tight_layout()
plt.show()