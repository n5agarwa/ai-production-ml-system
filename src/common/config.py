import yaml
from pathlib import Path

class AppConfig:
    @staticmethod
    def load(path="configs/base.yaml"):
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Config not found: {p.resolve()}")
        with p.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
