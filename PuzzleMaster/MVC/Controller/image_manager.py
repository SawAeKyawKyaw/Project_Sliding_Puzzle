# MVC/Controller/image_manager.py
# Controller module to manage puzzle image retrieval from the file system.

import os
from typing import List

PUZZLE_IMAGE_PATH = os.path.abspath("images/puzzle_images")

def get_available_images() -> List[str]:
    """
    Returns a list of available image filenames in the puzzle image directory.
    Filters by allowed image file extensions.
    """
    allowed_ext = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")
    if not os.path.exists(PUZZLE_IMAGE_PATH):
        return []
    return [
        f for f in os.listdir(PUZZLE_IMAGE_PATH)
        if f.lower().endswith(allowed_ext)
    ]
