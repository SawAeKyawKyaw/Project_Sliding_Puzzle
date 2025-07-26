# backend/service/image_service.py
# Service module for retrieving available puzzle image filenames.

from backend.model import image_model
from typing import List

def fetch_puzzle_images() -> List[str]:
    """
    Fetch a list of puzzle image filenames available for game selection.

    :return: List of image filenames as strings.
    """
    return image_model.get_available_images()
