# backend/service/highscore_service.py
# Service module for handling high score business logic.

from backend.model import score_model
from typing import List, Dict, Optional

def fetch_high_scores(limit: int = 10, difficulty: Optional[str] = None, sort_by: str = "duration") -> List[Dict[str, str | int]]:
    """
    Retrieve a list of top high scores, optionally filtered by difficulty
    and sorted by a chosen metric.

    :param limit: Number of top scores to return.
    :param difficulty: Optional filter for puzzle difficulty level.
    :param sort_by: Metric to sort scores by ('duration' or 'moves').
    :return: List of high score records.
    """
    return score_model.get_high_scores(limit=limit, difficulty=difficulty, sort_by=sort_by)

def save_game_record(duration: int, moves: int, difficulty: str, image_name: str) -> None:

    """
    Save a completed game record with gameplay statistics.

    :param duration: Completion time in seconds.
    :param moves: Number of moves taken to solve the puzzle.
    :param difficulty: Selected difficulty or grid size.
    :param image_name: Filename of the puzzle image used.
    """
    score_record:dict[str, str|int] = {
        "duration": duration,
        "moves": moves,
        "difficulty": difficulty,
        "image_name": image_name
    }

    score_model.save_score(score_record)
