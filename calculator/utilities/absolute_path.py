"""Script that holds absolute path utility function"""
from pathlib import Path


def absolute_path(filepath):
    """Method to get absolute path from a relative path"""
    relative = Path(filepath)
    return relative.absolute()
