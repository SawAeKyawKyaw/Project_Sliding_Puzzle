PuzzleMaster/
│
├── app.py                         # Flask entry
├── data/                          # All JSON files (highscores)
│     scores.json
│
├── images/
│     ├── miscellaneous_images/    # UI images
│     └── puzzle_images/           # Game images + uploads
│
├── MVC/
│     ├── Model/
│     │     highscore_model.py     
│     │     image_model.py         
│     ├── View/
│     │     routes.py              # all @app.route handlers
│     └── Controller/
│           image_manager.py               
│           score_controller.py
│     
├── static/
│     ├── css/
│     │     global.css
│     │     highscore.css
│     │     index.css
│     │     puzzle_settings.css
│     │     puzzle_play.css
│     ├── font/
│     │     PressStart2P-Regular.ttf
│     └── js/
│           highscore.js              
│           index.js
│           puzzle_play.js
│           puzzle_settings.js
|
├── test/
│     └── test_backend.py/                 # tests for the app
│
├── docs/
│     └── project_structure.md/ 
│
├── templates/
│       highscore.html              
│       index.html
│       puzzle_play.html
│       puzzle_settings.html
│
└── README.md                   

