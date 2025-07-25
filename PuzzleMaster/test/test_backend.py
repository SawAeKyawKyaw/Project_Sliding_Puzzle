import unittest
import os
import json
from datetime import datetime # type: ignore
from typing import List

# Import your modules (adjust if relative pathing differs)
from MVC.Controller import score_controller, image_manager

# Patch DATA_PATH to avoid modifying the real file
TEST_DATA_PATH = os.path.abspath("test/test_scores.json")
score_controller.DATA_PATH = TEST_DATA_PATH  # Redirect to test file

class TestScoreController(unittest.TestCase):
    def setUp(self):
        # Clean and write dummy test data
        self.sample_scores: list[dict[str , str | int]] = [
            {
                "id": 1,
                "date": "2025-07-14T12:00:00",
                "difficulty": "3x3",
                "duration": 100,
                "image_name": "image1.jpg",
                "moves": 50
            },
            {
                "id": 2,
                "date": "2025-07-14T12:05:00",
                "difficulty": "4x4",
                "duration": 200,
                "image_name": "image2.jpg",
                "moves": 80
            }
        ]
        with open(TEST_DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(self.sample_scores, f, indent=4)

    def tearDown(self):
        # Remove test file after tests
        if os.path.exists(TEST_DATA_PATH):
            os.remove(TEST_DATA_PATH)

    def test_load_scores(self):
        scores = score_controller.load_scores()
        self.assertEqual(len(scores), 2)
        self.assertEqual(scores[0]['difficulty'], "3x3")

    def test_save_score(self):
        new_record: dict[str, str | int] = {
            "difficulty": "3x3",
            "duration": 150,
            "image_name": "image3.jpg",
            "moves": 60
        }
        score_controller.save_score(new_record)
        scores = score_controller.load_scores()
        self.assertEqual(len(scores), 3)
        self.assertEqual(scores[-1]['image_name'], "image3.jpg")

    def test_get_high_scores(self):
        scores = score_controller.get_high_scores(limit=1, difficulty="4x4")
        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0]['difficulty'], "4x4")

class TestImageManager(unittest.TestCase):
    def test_get_available_images(self):
        image_list: List[str] = image_manager.get_available_images()
        self.assertIsInstance(image_list, list)
        for filename in image_list:
            self.assertTrue(filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")))

if __name__ == "__main__":
    unittest.main()
