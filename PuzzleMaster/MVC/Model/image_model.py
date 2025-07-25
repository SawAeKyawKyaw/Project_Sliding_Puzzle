# MVC/Model/image_model.py
# Model responsible for fetching available puzzle image filenames.

from MVC.Controller import image_manager
from typing import List

def fetch_puzzle_images() -> List[str]:
    """
    Retrieve the list of available puzzle image filenames.

    :return: List of image file names as strings.
    """
    return image_manager.get_available_images()
