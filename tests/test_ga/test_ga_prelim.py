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
from geometry.mask_definition import mask_definition
from optimization.ga.optimizer import GeneticAlgorithmOptimizer

PX_PER_UM = CONFIG["optics"]["grid_resolution_px_per_um"]
WINDOW_SIZE = CONFIG["optics"]["window_size_xy"]
SHAPE = CONFIG["optimization"]["spatial_dimensions"]
expected_children = CONFIG["optimization"]["children_from_crossover"]


start_total = time.perf_counter()

polygons = mask_definition()

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

ga = GeneticAlgorithmOptimizer(
    population_size=15,
    max_generations=30,
    random_seed=42,
    size = SHAPE,
    
)