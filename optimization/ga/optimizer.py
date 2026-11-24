"""
=================================================================================
AI ASSISTANCE DISCLOSURE - optimization/ga/optimizer.py
=================================================================================
This file was created with AI assistance. It provides a scaffold for the 
GeneticAlgorithmOptimizer class that orchestrates OPC mask pattern evolution.

Student verification required:
1. Read docstring explaining GA mathematical formulation and operators
2. Implement population initialization with configurable size
3. Implement selection, crossover, mutation operators
4. Verify crossover produces exactly n children from top-m parents
5. Test optimization loop terminates within max_generations limit

Date created: 2026-11-11
=================================================================================
"""

import numpy as np
from typing import Callable, Tuple
from config.config import CONFIG
from optimization.ga.population import initialize_population
from optimization.ga.selection import selection
from optimization.ga.mutation import mutation_apply
from optimization.ga.fitness import fitness
from optimization.ga.crossover import crossover_select
from optics.aerial_image import compute_aerial_image


# ================================================================================
# CLASS: GeneticAlgorithmOptimizer
# ================================================================================

class GeneticAlgorithmOptimizer:
    """
    Genetic algorithm optimized for OPC mask pattern search.
    
    Mathematical model of genetic algorithm:
      
      Phase 1: Population Initialization
        Create population_size individuals (mask configurations)
        Each individual represents a candidate solution to OPC problem
        
      Phase 2+: Evolutionary Loop (per generation):
        
        Step A: Fitness Evaluation
          For each individual, compute objective function value (printing error)
          Lower error = higher fitness for optimization
        
        Step B: Selection
          Select elite individuals based on fitness ranking
          Top k elites preserved unchanged to next generation
        
        Step C: Crossover  
          Selected parents undergo crossover operation
          Children inherit features from parent combination
        
        Step D: Mutation
          Apply random mutations to children (feature add/remove/modify)
          Maintains population size constant
        
        Step E: Elitism
          Best individuals preserved, replacing worst performers
  
      Termination criteria:
        - Max generations reached
        - Objective function reaches target threshold
        - Convergence detected (fitness plateau)
      
    Physical interpretation:
      Each individual in population represents a different photomask configuration.
      GA explores search space by combining good features and introducing variation.
      
    TODO-ga-population-initialization: 
      Implement initialization of population_size mask chromosomes
      
    TODO-ga-selection-implementation:
      Implement selection to pick top k individuals based on fitness ranking
      
      Selection approach options:
        1. Tournament selection: Randomly select subset, keep best
        2. Roulette wheel: Probability proportional to fitness
        3. Rank-based selection: Sort by fitness, select top portion
        
      For simple OPC problem, rank-based is adequate.
      
    TODO-ga-crossover-implementation: 
      Implement crossover operation between selected parents
      
      Cross-over strategy for mask features:
        - Extract rectangles from parent1 and parent2
        - Combine into children preserving geometric validity  
        - Or inherit all features from one parent (no crossover, just selection)
        
      
    TODO-ga-mutation-implementation: 
      Implement mutation operation
      
      Mutation strategies for OPC mask features:
        1. Add random small rectangle feature to child
        2. Remove random feature from child  
        3. Slightly modify dimensions or position of existing feature
        
      Mutation rate controls probability each feature is mutated.
      
    TODO-ga-evolutionary-loop-implementation:
      Implement main optimization loop that runs until termination.
      
    Raises:
      ValueError: If population_size invalid or max_generations negative
      RuntimeError: If optimization fails (no feasible solutions found)
      
    Attributes after initialization:
      - population: List of MaskFeature objects (chromosomes)
      - best_fitness_history: List tracking best fitness per generation
      
    Example usage after implementation complete:
      
      ga = GeneticAlgorithmOptimizer(
          population_size=15,
          max_generations=30,
          random_seed=42
      )
      
      result = ga.optimize(objective_function=my_error_metric)
      
      print(f"Best solution fitness: {result.best_fitness}")
      print(f"Evaluations used: {ga.evaluations}")

    Implementation after TODO markers below...
    """
    
    def __init__(
        self,
        population_size: int = CONFIG["optimization"]["population_size"],
        max_generations: int = CONFIG["optimization"]["max_generations"],
        seed: int = CONFIG["experiment"]["random_seed"],
        shape: Tuple[int, int] = CONFIG["optimization"]["spatial_dimensions"],
        expected_children: int = CONFIG["optimization"]["children_from_crossover"]
    ):

        # Store the genetic algorithm configuration.
        self.population_size = population_size
        self.shape = shape
        self.max_generations = max_generations
        self.expected_children = expected_children
        self.seed = seed

        # Set the random seed for reproducible optimization experiments.
        np.random.seed(self.seed)

    def optimize(
        self,
        objective_function: Callable,
        target_pattern: np.ndarray,
        initial_mask: np.ndarray,
        progress_callback: Callable | None = None
    ) -> np.ndarray:

        # Convert the target pattern and initial mask into NumPy arrays.
        target_pattern = np.asarray(target_pattern, dtype=float)
        initial_mask = np.asarray(initial_mask, dtype=float)

        # Verify that both inputs are two-dimensional arrays.
        if target_pattern.ndim != 2 or initial_mask.ndim != 2:
            raise ValueError(
                "Target pattern and initial mask must both be 2D arrays."
            )

        # Verify that the initial mask and target pattern have matching dimensions.
        if initial_mask.shape != target_pattern.shape:
            raise ValueError(
                f"Initial mask shape {initial_mask.shape} does not match "
                f"target pattern shape {target_pattern.shape}."
            )

        # Verify that the initial mask matches the configured dimensions.
        if initial_mask.shape != tuple(self.shape):
            raise ValueError(
                f"Initial mask shape {initial_mask.shape} does not match "
                f"configured dimensions {tuple(self.shape)}."
            )

        # Calculate the expected number of retained parents.
        expected_parents = self.population_size - self.expected_children

        # Verify that the expected parent count is positive.
        if expected_parents <= 0:
            raise ValueError(
                "Expected children must be smaller than population size."
            )

        # Initialize the population using the original rasterized mask.
        current_population = initialize_population(
            initial_mask,
            self.population_size
        )

        # Verify that the initial population has the expected size.
        if len(current_population) != self.population_size:
            raise RuntimeError(
                f"Initial population size is {len(current_population)}. "
                f"Expected {self.population_size}."
            )

        # Initialize the best solution using the original mask.
        best_solution = initial_mask.copy()

        # Calculate the aerial image produced by the initial mask.
        best_aerial_image = compute_aerial_image(best_solution)

        # Evaluate the initial mask against the desired geometric pattern.
        best_fitness = fitness(
            target_pattern,
            best_aerial_image
        )

        # Execute the genetic algorithm for the configured number of generations.
        for generation in range(self.max_generations):

            # Select the highest-performing individuals from the current population.
            selected = selection(
                current_population,
                target_pattern
            )

            # Verify that selection returned the expected number of parents.
            if len(selected) != expected_parents:
                raise RuntimeError(
                    f"Selected {len(selected)} parents. "
                    f"Expected {expected_parents}."
                )

            # Generate new individuals through crossover.
            children = crossover_select(
                selected,
                self.expected_children
            )

            # Verify that crossover produced the expected number of children.
            if len(children) != self.expected_children:
                raise RuntimeError(
                    f"Generated {len(children)} children. "
                    f"Expected {self.expected_children}."
                )

            # Apply mutations within the permitted region around the original mask.
            mutated = mutation_apply(
                children,
                reference_mask=initial_mask
            )

            # Verify that mutation preserved the expected number of children.
            if len(mutated) != self.expected_children:
                raise RuntimeError(
                    f"Generated {len(mutated)} mutated children. "
                    f"Expected {self.expected_children}."
                )

            # Evaluate the fitness of each mutated individual.
            for individual_index, individual in enumerate(mutated):

                # Calculate the aerial image produced by the candidate mask.
                aerial_image = compute_aerial_image(individual)

                # Calculate the candidate's fitness against the desired pattern.
                score = fitness(
                    target_pattern,
                    aerial_image
                )

                # Update the best solution if the candidate has lower error.
                if score < best_fitness:
                    best_fitness = score
                    best_solution = individual.copy()
                    best_aerial_image = aerial_image.copy()

                # Update the live visualization every 10 evaluated children.
                if progress_callback is not None and (
                    (individual_index + 1) % 10 == 0
                    or individual_index == len(mutated) - 1
                ):

                    # Send the current best solution and its aerial image to the callback.
                    progress_callback(
                        generation + 1,
                        best_solution,
                        best_fitness,
                        best_aerial_image,
                        individual_index + 1,
                        len(mutated)
                    )

            # Combine selected parents and mutated children into the next generation.
            current_population = np.concatenate(
                (selected, mutated),
                axis=0
            )

            # Verify that the population size remains constant.
            if len(current_population) != self.population_size:
                raise RuntimeError(
                    f"Population size changed to {len(current_population)}. "
                    f"Expected {self.population_size}."
                )

            # Report the best fitness achieved in the current generation.
            print(
                f"Generation {generation + 1}/{self.max_generations} | "
                f"Best MSE: {best_fitness:.8e}"
            )

        # Return the best-performing mask found during optimization.
        return best_solution
