import os
from pathlib import Path


class Config:
    """Configuration class for the resume application."""

    def __init__(self):
        self.data_path = self.get_path_from_env(
            "RESUME_DATA_PATH",
            "./data/data.json",
            exists=True
        )
        self.disable_overwrites = self.get_boolean_from_env(
            "RESUME_DISABLE_OVERWRITES",
            default=False
        )
        self.overwrites_path = self.get_path_from_env(
            "RESUME_OVERWRITE_PATH",
            "./data/overwrites.json",
            exists=False
        )
        self.debug = self.get_boolean_from_env(
            "RESUME_DEBUG",
            default=False
        )

    @staticmethod
    def get_boolean_from_env(var_name, default=False):
        """Get a boolean value from an environment variable.

        Args:
            var_name (str): The name of the environment variable.
            default (bool): The default value if the variable is not set.

        Returns:
            bool: The boolean value of the environment variable, or the default
                if not set.
        """

        value = os.getenv(var_name, str(default)).lower()
        return value in ("true", "1", "yes", "y")

    @staticmethod
    def get_path_from_env(var_name, default, is_dir=False, exists=True):
        """Get a path from an environment variable.

        Args:
            var_name (str): The name of the environment variable.
            default (str): The default path if the variable is not set.
            is_dir (bool): Whether the path should be a directory.
            exists (bool): Whether the path should exist.

        Returns:
            Path: The validated path from the environment variable.

        Raises:
            ValueError: If the path does not exist or is not a directory when
                expected.
        """

        env_path = Path(os.getenv(var_name, default))
        if is_dir and not env_path.is_dir():
            raise ValueError(
                f"Expected directory at '{env_path}',"
                f"but it does not exist or is not a directory."
            )

        if exists and not env_path.exists():
            raise ValueError(
                f"Expected path at '{env_path}', but it does not exist.")

        return env_path


CONFIG = Config()
