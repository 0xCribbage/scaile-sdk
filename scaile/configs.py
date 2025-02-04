# scaile/config.py

from pathlib import Path
import os
from typing import Dict, Any
import yaml
from dotenv import load_dotenv
import os

class Config:
    DEBUG = os.getenv("SCAILE_DEBUG", "False").lower() == "true"

    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "default_secret_key")
    
class Settings:
    def __init__(self, env: str = "development"):
        """Initialize settings with the specified environment."""
        self.env = env
        self.base_dir = Path(__file__).parent.parent
        
        # Load environment variables from .env file
        load_dotenv(self.base_dir / f".env.{env}")
        
        # Load configuration from YAML
        self.config = self._load_config()
        
        # Override with environment variables
        self._override_from_env()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        config_path = self.base_dir / "configs" / f"config.{self.env}.yaml"
        with open(config_path) as f:
            return yaml.safe_load(f)
    
    def _override_from_env(self) -> None:
        """Override configuration with environment variables."""
        for key in self.config.keys():
            env_key = f"SCAILE_{key.upper()}"
            if env_value := os.getenv(env_key):
                self.config[key] = env_value
    
    def __getattr__(self, name: str) -> Any:
        """Get configuration value by attribute name."""
        if name in self.config:
            return self.config[name]
        raise AttributeError(f"No configuration found for: {name}")

# Create default settings instance
settings = Settings(os.getenv("SCAILE_ENV", "development"))