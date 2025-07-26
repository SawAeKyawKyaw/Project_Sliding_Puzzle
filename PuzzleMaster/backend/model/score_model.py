# backend/model/score_model.py
# Model module responsible for loading, saving, and retrieving game score data from the JSON file.


import json
import os
from datetime import datetime
from typing import List, Dict, Optional

# Path to the JSON file where scores are stored
DATA_PATH = os.path.abspath("data/scores.json")

# Type alias for a score record
ScoreRecord = Dict[str, str | int]

def load_scores() -> List[ScoreRecord]:
    """
    Load all score records from the scores.json file.
    Returns an empty list if the file does not exist.
    """
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_score(score_record: Dict[str, str | int]) -> None:
    """
    Append a new score record to the score file.
    Automatically assigns an ID and timestamp.
    """
    scores = load_scores()
    score_record['id'] = len(scores) + 1
    score_record['date'] = datetime.now().isoformat()
    scores.append(score_record)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=4)

def get_high_scores(limit: int = 10, difficulty: Optional[str] = None, sort_by: str = "duration") -> List[ScoreRecord]:
    """
    Retrieve top scores sorted by a specified key (default: duration).
    Can be filtered by puzzle difficulty.
    """
    scores = load_scores()
    if difficulty:
        scores = [s for s in scores if s["difficulty"] == difficulty]
    return sorted(scores, key=lambda x: x[sort_by])[:limit]

