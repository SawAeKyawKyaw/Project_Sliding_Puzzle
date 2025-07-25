# PuzzleMaster

## Overview  
PuzzleMaster is a sliding puzzle web application built with Flask (Python) using the MVC architecture. The game features customizable puzzles, score tracking, and an interactive user interface.

## Features  
- Interactive sliding puzzle gameplay  
- Upload and use custom puzzle images  
- Track high scores saved in JSON format  
- Responsive and clean UI with CSS and JavaScript  
- MVC structure for clear separation of concerns  

## Folder Structure  
PuzzleMaster/
│
├── app.py # Flask application entry point
├── data/ # JSON files storing highscores
│ └── scores.json
├── images/ # All game and UI images
│ ├── miscellaneous_images/ # UI images
│ └── puzzle_images/ # Game images and user uploads
├── MVC/ # Model-View-Controller components
│ ├── Model/
│ │ ├── highscore_model.py
│ │ └── image_model.py
│ ├── View/
│ │ └── routes.py # Flask route handlers
│ └── Controller/
│ ├── image_manager.py
│ └── score_controller.py
├── static/ # Static assets (CSS, fonts, JS)
│ ├── css/
│ ├── font/
│ └── js/
├── test/ # Unit tests
│ └── test_backend.py
├── docs/ # Documentation files
│ └── project_structure.md
├── templates/ # HTML templates for Flask
└── README.md # Project documentation

bash
Copy
Edit

## Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/PuzzleMaster.git
Navigate into the project folder:

bash
Copy
Edit
cd PuzzleMaster
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app:

bash
Copy
Edit
flask run
or

bash
Copy
Edit
python app.py
Usage
Open your web browser and navigate to http://localhost:5000

Use the UI to play sliding puzzles, upload images, and check high scores

Dependencies
Flask

(Add others here if you have more)
