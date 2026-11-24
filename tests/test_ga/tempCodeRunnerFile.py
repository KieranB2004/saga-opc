
import sys
from pathlib import Path

# Add the project root to the Python module search path.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import time
import numpy as np
import matplotlib.pyplot as plt
from shapely import Polygon

from config.config import CONFIG
from geometry.convert_to_simulation_grid import convert_to_simulation_grid
from geometry.mask_definition import mask_definition
from optics.aerial_image import compute_aerial_image
from optimization.ga.optimizer import GeneticAlgorithmOptimizer
from optimization.ga.fitness import fitness


# Retrieve the simulation and optimization configuration.
PX_PER_UM = CONFIG["optics"]["grid_resolution_px_per_um"]
WINDOW_SIZE = CONFIG["optics"]["window_size_xy"]
SHAPE = CONFIG["optimization"]["spatial_dimensions"]
EXPECTED_CHILDREN = CONFIG["optimization"]["children_from_crossover"]

# Start measuring the total simulation and setup time.
start_total = time.perf_counter()

# Generate the desired geometric mask polygons.
polygons = mask_definition()

# Convert the desired polygons into a binary simulation grid.
output_grid = convert_to_simulation_grid(
    polygons=polygons,
    grid_resolution_px_per_um=PX_PER_UM
)

# Calculate the aerial image produced by the original mask.
fft_output_grid = compute_aerial_image(output_grid)

# Retrieve the intensity threshold used to simulate resist development.
threshold = CONFIG["printing"]["default_intensity_threshold"]

# Calculate the developed pattern produced by the original mask.
developed_mask = fft_output_grid >= threshold

# Display the original developed pattern and desired polygon outlines.
fig, ax = plt.subplots(figsize=(8, 6))

im = ax.imshow(
    developed_mask,
    cmap="Blues",
    origin="lower"
)

ax.set_xlabel(f"X (pixels) / ({1000 / PX_PER_UM:.2f} nm per pixel)")
ax.set_ylabel(f"Y (pixels) / ({1000 / PX_PER_UM:.2f} nm per pixel)")

# Overlay the desired geometric pattern outlines.
for poly_points, _ in polygons:

    # Convert polygon coordinates from micrometres to pixels.
    pixels = (np.array(poly_points) * PX_PER_UM).tolist()

    # Create a Shapely polygon for plotting.
    poly = Polygon(pixels)

    # Plot the polygon boundary.
    ax.plot(
        poly.exterior.xy[0],
        poly.exterior.xy[1],
        color="black",
        linewidth=4,
        linestyle="solid"
    )

# Configure the initial visualization.
ax.set_title("Initial Developed Pattern")
step = 16
ax.set_xticks(range(0, WINDOW_SIZE, step))
ax.set_yticks(range(0, WINDOW_SIZE, step))

plt.tight_layout()

# Stop measuring the initial simulation and setup time.
end_total = time.perf_counter()
print(f"Initial simulation time: {end_total - start_total:.4f} seconds")

# Print the dimensions of the target and simulation arrays.
print("\n--- GA DIMENSION DIAGNOSTICS ---")
print("Output grid:", output_grid.shape)
print("Target aerial image:", fft_output_grid.shape)
print("SHAPE configuration:", SHAPE)
print("--------------------------------\n")

# Initialize the genetic algorithm optimizer.
ga = GeneticAlgorithmOptimizer(
    population_size=15,
    max_generations=30,
    seed=777,
    shape=SHAPE,
    expected_children=EXPECTED_CHILDREN
)

# Start measuring the optimization time.
start_optimization = time.perf_counter()

# Run the genetic algorithm using the desired geometric pattern as the target.
best_mask = ga.optimize(
    objective_function=None,
    target_pattern=output_grid,
    initial_mask=output_grid
)

# Stop measuring the optimization time.
end_optimization = time.perf_counter()

print(
    f"Optimization completed in "
    f"{end_optimization - start_optimization:.4f} seconds"
)

# Calculate the aerial image produced by the optimized mask.
best_aerial_image = compute_aerial_image(best_mask)

# Calculate the final fitness using the desired geometric pattern.
final_fitness = fitness(
    output_grid,
    best_aerial_image
)

print(f"Final MSE: {final_fitness:.8e}")

# Convert the optimized aerial image into a binary developed pattern.
optimized_developed_mask = best_aerial_image >= threshold

# Calculate the number of pixels that differ from the desired pattern.
final_error = np.sum(
    np.abs(
        optimized_developed_mask.astype(int) -
        output_grid.astype(int)
    )
)

print(f"Final pixel error: {final_error}")

# Display the optimized mask.
fig2, ax2 = plt.subplots(figsize=(8, 6))

ax2.imshow(
    best_mask,
    cmap="Blues",
    origin="lower"
)

ax2.set_xlabel("X (pixels)")
ax2.set_ylabel("Y (pixels)")
ax2.set_title(f"Optimized Mask Result (MSE: {final_fitness:.8e})")

plt.tight_layout()

# Save the optimized mask visualization.
plt.savefig("optimized_result.png")
print("Result saved to 'optimized_result.png'")

# Display the generated figures.
plt.show()
