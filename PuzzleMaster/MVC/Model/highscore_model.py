# MVC/Model/highscore_model.py
# Model responsible for managing score data logic.

from MVC.Controller import score_controller
from typing import List, Dict, Optional

def fetch_high_scores(limit: int = 10, difficulty: Optional[str] = None, sort_by: str = "duration") -> List[Dict[str, str | int]]:
    """
    Fetch high scores from the score controller.

    :param limit: Number of scores to retrieve
    :param difficulty: Optional filter by puzzle difficulty
    :param sort_by: Metric to sort by ('duration' or 'moves')
    :return: List of score records
    """
    return score_controller.get_high_scores(limit=limit, difficulty=difficulty, sort_by=sort_by)

def save_game_record(duration: int, moves: int, difficulty: str, image_name: str) -> None:

    """
    Save a new game record to the score file.

    :param duration: Completion time in seconds
    :param moves: Number of moves taken
    :param difficulty: Game difficulty level
    :param image_name: Image used in the puzzle
    """
    score_record:dict[str, str|int] = {
        "duration": duration,
        "moves": moves,
        "difficulty": difficulty,
        "image_name": image_name
    }

    score_controller.save_score(score_record)
