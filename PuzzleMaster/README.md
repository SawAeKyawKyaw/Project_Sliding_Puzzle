# Puzzle Master

## 1. Overview
    Puzzle Master is a fully offline, web-based sliding puzzle game built with Flask.  
    It tracks player scores based on moves and time taken to solve puzzles.  
    The project uses a clean MVC architecture to ensure scalability and ease of future expansions, such as adding new game modes or features.

## 2. Features
- Fully offline gameplay — no internet connection required  
- Sliding puzzle game with multiple puzzle images  
- Option to choose difficulty by selecting grid size (e.g., 3x3, 4x4)  
- Ability to select different puzzle images for gameplay  
- Score tracking based on the number of moves and elapsed time  
- Clean Model-View-Controller (MVC) architecture for modularity and scalability  
- JSON-based highscore storage for easy data management  
- Responsive UI with organized static assets (CSS, JS, images)  
- Future-ready design to support additional game modes or features

## 3. Folder Structure (Optional but helpful)
```
PuzzleMaster/
│
├── app.py # Flask entry
├── data/ # All JSON files (highscores)
│ └── scores.json
├── images/
│ ├── miscellaneous_images/ # UI images
│ └── puzzle_images/ # Game images + uploads
├── backend/
│ ├── model/
│ │ ├── score_model.py         # handles reading/writing scores
│ │ └── image_model.py         # fetch image filenames
│ ├── service/
│ │ ├── highscore_service.py   # handles the logic
│ │ └── image_service.py          
│ └── routes/
│   └── routes.py              # all @app.route endpoints
├── static/
│ ├── css/
│ │ ├── global.css
│ │ ├── highscore.css
│ │ ├── index.css
│ │ ├── puzzle_settings.css
│ │ └── puzzle_play.css
│ ├── font/
│ │ └── PressStart2P-Regular.ttf
│ └── js/
│ ├── highscore.js
│ ├── index.js
│ ├── puzzle_play.js
│ └── puzzle_settings.js
├── test/
│ └── test_backend.py # tests for the app
├── docs/
│ └── project_structure.md
├── templates/
│ ├── highscore.html
│ ├── index.html
│ ├── puzzle_play.html
│ └── puzzle_settings.html
└── README.md
```

## 4. Installation
### Prerequisites
- Python 3.x installed
- Git installed (optional if cloning)

### Steps
1. Clone the repository
```
[Cloning repo](https://github.com/SawAeKyawKyaw/Project_Sliding_Puzzle)
cd Puzzle Master
```

2. Create and activate a virtual environment
- On Windows:
```
python -m venv venv
.\venv\Scripts\activate
```

- On MacOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install Flask
```
pip install flask
```

## 5. Usage
To start the Puzzle Master app:
```
# From inside the PuzzleMaster folder (and with virtual environment activated if used)
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000/
```

### How to play:
- Choose difficulty by selecting grid size and images.
- Play the sliding puzzle.
- Your score is tracked based on moves and timer.
- Scores are saved locally (offline).

## 6. Dependencies
The project requires the following Python package:

- **Flask** — used as the backend web framework

All other modules (`os`, `typing`, `datetime`, `uuid`) are built-in Python libraries and do not require separate installation.

To install Flask:

```
pip install flask
```

## 7. Future Work

- Implement image upload functionality  
- Add new puzzle types and game modes  
- Enhance UI/UX with animations and sounds


## 8. Contact
saw.ae.kyaw.kyaw.sakk@gmail.com
