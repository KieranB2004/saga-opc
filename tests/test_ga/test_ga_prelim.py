
import sys
from pathlib import Path

# Add the project root to the Python module search path.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import time
import numpy as np
import matplotlib.pyplot as plt

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
MAX_GEN = CONFIG["optimization"]["max_generations"]
POPULATION_SIZE = CONFIG["optimization"]["population_size"]

# Retrieve the intensity threshold used to simulate resist development.
threshold = CONFIG["printing"]["default_intensity_threshold"]

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

# Calculate the developed pattern produced by the original mask.
developed_mask = fft_output_grid >= threshold

# Stop measuring the initial simulation and setup time.
end_total = time.perf_counter()
print(f"Initial simulation time: {end_total - start_total:.4f} seconds")

# Print the dimensions of the target and simulation arrays.
print("\n--- GA DIMENSION DIAGNOSTICS ---")
print("Output grid:", output_grid.shape)
print("Target aerial image:", fft_output_grid.shape)
print("SHAPE configuration:", SHAPE)
print("Population size:", POPULATION_SIZE)
print("Maximum generations:", MAX_GEN)
print("Expected children:", EXPECTED_CHILDREN)
print("--------------------------------\n")

# Calculate the initial fitness.
initial_fitness = fitness(
    output_grid,
    fft_output_grid
)

# Calculate the initial pixel error.
initial_error = np.sum(
    np.abs(
        developed_mask.astype(int) -
        output_grid.astype(int)
    )
)

# Create a single figure containing all four pattern visualizations.
plt.ion()

fig, axes = plt.subplots(
    1,
    4,
    figsize=(20, 6)
)

# Display the initial mask pattern.
im0 = axes[0].imshow(
    output_grid,
    cmap="Blues",
    origin="upper",
    vmin=0,
    vmax=1,
    interpolation="nearest"
)

axes[0].set_title("Initial Mask Pattern")

# Display the developed pattern produced by the original mask.
im1 = axes[1].imshow(
    developed_mask,
    cmap="Blues",
    origin="upper",
    vmin=0,
    vmax=1,
    interpolation="nearest"
)

axes[1].set_title("Initial Developed Pattern")

# Display the initial mask as the starting optimized mask.
im2 = axes[2].imshow(
    output_grid,
    cmap="Blues",
    origin="upper",
    vmin=0,
    vmax=1,
    interpolation="nearest"
)

axes[2].set_title("Optimized Mask Pattern")

# Display the initial developed pattern as the starting optimized pattern.
im3 = axes[3].imshow(
    developed_mask,
    cmap="Blues",
    origin="upper",
    vmin=0,
    vmax=1,
    interpolation="nearest"
)

axes[3].set_title("Optimized Developed Pattern")

# Configure the axes for all four visualizations.
step = 16

for ax in axes:

    # Configure the spatial axis labels.
    ax.set_xlabel(f"X (pixels) / ({1000 / PX_PER_UM:.2f} nm per pixel)")
    ax.set_ylabel(f"Y (pixels) / ({1000 / PX_PER_UM:.2f} nm per pixel)")

    # Configure the spatial axis tick marks.
    ax.set_xticks(range(0, WINDOW_SIZE, step))
    ax.set_yticks(range(0, WINDOW_SIZE, step))

# Add an overall figure title.
fig.suptitle(
    f"OPC Genetic Algorithm | Initial MSE: {initial_fitness:.8e} | "
    f"Pixel Error: {initial_error}",
    fontsize=14
)

# Adjust spacing between the four visualizations.
plt.tight_layout(rect=[0, 0, 1, 0.92])

# Display the figure without blocking the genetic algorithm.
plt.show(block=False)
plt.pause(0.1)


# Define the callback used to update the live visualization.
def update_plot(
    generation,
    best_mask,
    best_fitness,
    best_aerial_image,
    evaluated_children=None,
    total_children=None
):

    # Convert the best aerial image into a binary developed pattern.
    optimized_developed_mask = best_aerial_image >= threshold

    # Calculate the number of pixels that differ from the desired pattern.
    final_error = np.sum(
        np.abs(
            optimized_developed_mask.astype(int) -
            output_grid.astype(int)
        )
    )

    # Update the optimized mask visualization.
    im2.set_data(best_mask)

    # Update the optimized developed pattern visualization.
    im3.set_data(optimized_developed_mask)

    # Configure the current optimization progress text.
    if evaluated_children is not None:
        progress_text = (
            f"Generation {generation}/{MAX_GEN} | "
            f"Child {evaluated_children}/{total_children}"
        )
    else:
        progress_text = f"Generation {generation}/{MAX_GEN}"

    # Update the overall figure title with the current optimization results.
    fig.suptitle(
        f"{progress_text} | "
        f"Best MSE: {best_fitness:.8e} | "
        f"Pixel Error: {final_error}",
        fontsize=14
    )

    # Refresh the figure.
    fig.canvas.draw_idle()
    fig.canvas.flush_events()
    plt.pause(0.001)


# Initialize the genetic algorithm optimizer.
ga = GeneticAlgorithmOptimizer(
    population_size=POPULATION_SIZE,
    max_generations=MAX_GEN,
    seed=CONFIG["experiment"]["random_seed"],
    shape=SHAPE,
    expected_children=EXPECTED_CHILDREN
)

# Start measuring the optimization time.
start_optimization = time.perf_counter()

# Run the genetic algorithm using the desired geometric pattern as the target.
best_mask = ga.optimize(
    objective_function=None,
    target_pattern=output_grid,
    initial_mask=output_grid,
    progress_callback=update_plot
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

# Print the numerical ranges of the final visualization arrays.
print("\n--- FINAL VISUALIZATION DIAGNOSTICS ---")
print("Initial mask:", np.unique(output_grid))
print("Initial developed pattern:", np.unique(developed_mask))
print("Optimized mask:", np.unique(best_mask))
print("Optimized developed pattern:", np.unique(optimized_developed_mask))
print("Initial mask occupied pixels:", np.sum(output_grid))
print("Optimized mask occupied pixels:", np.sum(best_mask))
print("---------------------------------------\n")

# Update the visualization with the final optimization results.
update_plot(
    MAX_GEN,
    best_mask,
    final_fitness,
    best_aerial_image
)

# Force the final figure to render before saving.
fig.canvas.draw()

# Define the output path for the comparison figure.
output_path = PROJECT_ROOT / "ga_pattern_comparison.png"

# Save the complete comparison figure.
fig.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

print(f"Comparison figure saved to '{output_path}'")

# Keep the final figure open after optimization completes.
plt.ioff()
plt.show()
