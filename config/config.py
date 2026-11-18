import yaml
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONFIG_PATH = PROJECT_ROOT / "config" / "parameters.yaml"

with open(CONFIG_PATH, "r") as file:
    CONFIG = yaml.safe_load(file)
