import yaml
from pathlib import Path


# Locate the project root directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Locate the YAML configuration file.
CONFIG_PATH = PROJECT_ROOT / "config" / "parameters.yaml"


# Load the YAML configuration once.
with open(CONFIG_PATH, "r") as file:
    CONFIG = yaml.safe_load(file)
