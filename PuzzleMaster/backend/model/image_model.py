# backend/model/image_model.py
# Model module for accessing puzzle image filenames from the file system.

import os
from typing import List

PUZZLE_IMAGE_PATH = os.path.abspath("images/puzzle_images")

def get_available_images() -> List[str]:
    """
    Retrieve a list of image filenames from the puzzle image directory.

    Filters and returns only files with supported image extensions.

    :return: List of image filenames.
    """
    allowed_ext = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")
    if not os.path.exists(PUZZLE_IMAGE_PATH):
        return []
    return [
        f for f in os.listdir(PUZZLE_IMAGE_PATH)
        if f.lower().endswith(allowed_ext)
    ]
