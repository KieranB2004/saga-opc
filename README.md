# SAGA-OPC: Surrogate-Assisted Genetic Algorithm for Optical Proximity Correction

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)  
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## AI Usage Disclosure

This project was developed with AI assistance using OpenCode tooling. All files include AI usage disclosure headers at the top for academic integrity compliance. The University of Alberta Student Academic Integrity Policy applies: all AI-generated code must be independently verified by the student.

**Date of initial AI-assisted development:** November 09, 2026

---

## Project Overview

### Purpose

This project develops a Python-based computational simulator for simplified 193 nm deep ultraviolet (DUV) photolithography optical proximity correction (OPC). The system investigates whether Gaussian process surrogate models can reduce the number of expensive objective function evaluations required during mask optimization while maintaining acceptable printed-pattern accuracy.

### Research Question

**Can surrogate-assisted genetic algorithm (SAGA) reduce computational cost compared to conventional genetic algorithm (GA)?**

---

## Features

- Fourier-domain optical simulation using FFT-based scalar diffraction theory
- Simple threshold resist model for predicted pattern formation  
- Genetic algorithm with configurable population size, crossover, mutation
- Gaussian process surrogate for expensive function approximation
- Surrogate-assisted optimization framework
- Multiple error metrics (IoU, area error, edge placement)
- Experiment tracking and statistical comparison
- Visualization tools for optimization progress and pattern comparison

### Project Limitations

- Simplified scalar imaging model (not full industry-standard optical simulation)
- Coherent illumination approximation (no partial coherence initially)
- Threshold-based resist model (no complex chemical kinetics)
- Rectangular feature representation only  
- Geometric approximations, not experimentally validated

---

## Requirements

### Python Version

- Python 3.9 or higher

### Dependencies

Install with: `pip install -r requirements.txt`

Required packages (see `requirements.txt`):
- numpy (numerical computing)
- scipy (scientific functions, FFT)
- matplotlib (visualization)  
- scikit-learn (Gaussian process models)
- pyyaml (configuration parsing)
- pytest (testing framework)

### Hardware Requirements

- Minimal: Any modern laptop (4+ GB RAM recommended)
- Recommended: 8+ GB RAM for larger pattern simulations
- GPU not required (CPU-based computation)

---

## Installation

```bash
# Clone or navigate to repository
cd /path/to/opencode-engineering-validation

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# Or: venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import numpy, scipy, matplotlib, sklearn; print('All packages installed successfully')"
```

---

## Usage

### Run an Experiment

```bash
python experiments/run_experiment.py \
    --name my_experiment \
    --config config/parameters.yaml \
    --method saga
```

### Run Conventional GA for Comparison

```bash
python experiments/run_experiment.py \
    --name ga_baseline \
    --config config/parameters.yaml \
    --method ga
```

### Command-Line Interface (TBD - to be implemented)

To be implemented after optimization module is complete.

---

## Configuration

All simulation parameters are controlled via YAML files in `config/` directory:

- **config/parameters.yaml** - Primary configuration with all tunable parameters
  - Population size, crossover settings
  - Initial training points for surrogate  
  - Grid resolution, optical parameters
  - Error metric thresholds

### Key Configuration Parameters

```yaml
optimization:
  population_size: 15              # GA individuals per generation
  max_generations: 30              # Termination limit
  
surrogate:
  initial_training_points: 10      # Initial GP training set size
  update_frequency_generations: 5   # Retrain every N generations

optics:
  wavelength_nm: 0.193             # 193 nm DUV exposure
  numerical_aperture: 0.93         # NA value (fixed initially)
  grid_resolution_px_per_um: 5    # ~200nm/pixel resolution
```

---

## Testing

Run unit tests:

```bash
pytest tests/ -v
```

Run integration tests:

```bash  
pytest tests/integration/ -v
```

### Test Coverage Goals

- Geometry module: 100% of public functions tested
- Optics module: FFT cases, edge frequencies verified
- Mask module: All mutation/crossover variants covered  
- Optimization: GA convergence on simple problems
- Surrogate: GP training and prediction accuracy

---

## Project Structure

```
opencode-engineering-validation/
├── config/                # Configuration YAML files
│   └── parameters.yaml    # Main configuration
├── geometry/              # GDSII import and coordinate transforms
│   ├── import_gds.py     # TODO: Parse .gds files
│   └── ...               # More geometry utilities
├── optics/                # Fourier-domain optical simulation
│   ├── aerial_image.py   # FFT-based imaging computation
│   └── frequency_response.py  # OTF calculation  
├── mask/                  # GA chromosome representation
│   └── chromosome.py     # MaskFeature class
├── metrics/               # Error metric calculations
├── printing/              # Resist threshold model
├── optimization/          # Genetic algorithm implementation
│   ├── ga/               # GA operators
│   └── saga/             # SAGA orchestrator
├── surrogate/             # Gaussian process models
├── visualization/         # Plotting and figures
├── experiments/           # Experiment tracking and analysis
├── tests/                 # Unit and integration tests
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── .gitignore             # Git ignore patterns
```

---

## Academic Integrity Notice

This project uses AI assistance for scaffolding, documentation templates, and explanation. **All student implementations must be independently verified** as per University of Alberta Student Academic Integrity Policy:

- Students should complete TODO markers in each file
- AI-generated code must be reviewed and tested by the student
- All final implementations are student responsibility

See `AI_USAGE.md` for detailed disclosure documentation (to be created).

---

## Contributing

To contribute to this research project:

1. Fork the repository
2. Create a feature branch from main
3. Make your changes following existing patterns  
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit pull request

See `CONTRIBUTING.md` for detailed guidelines (to be created).

---

## Citation

When using results from this project in academic work:

```bibtex
@misc{saga-opc-project,
  title={SAGA-OPC: Surrogate-Assisted Genetic Algorithm for Optical Proximity Correction},
  author={},
  year={2026},
  note={Student research project at University of Alberta}
}
```

(Replace with actual citation information when complete)

---

## License

MIT License - see `LICENSE` file (to be created) for details.

---

## Acknowledgments

- Academic supervision and guidance provided throughout development
- OpenCode platform for AI-assisted scaffolding  
- scikit-learn library for Gaussian process implementation
- University of Alberta computational research resources

---

## Contact

For questions or issues: [Insert contact information]

---

**Version:** 0.1.0-dev (under active development)  
**Last updated:** November 2026
