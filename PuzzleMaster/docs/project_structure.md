project/
│
├── app.py                         # Flask entry
├── data/                          # All JSON files (highscores, session)
│     highscores.json
│     sessions.json
│
├── images/
│     ├── miscellaneous_images/    # UI images
│     └── puzzle_images/           # Game images + uploads
│
├── MVC/
│     ├── Model/
│     │     puzzle_state.py        # e.g., image ID, tile order
│     │     data_store.py          # load/save JSON
│     ├── View/
│     │     routes.py              # all @app.route handlers
│     ├── Controller/
│     │     logic.py               # win check, move handler, etc.
│     └── Database/
│           database.py            # access database
│
├── static/
│     ├── css/
│     │     style.css
│     └── js/
│           puzzle.js              # board logic
│           ui.js
│           controller.js
|
├── test/
│     └── test.py/                 # tests for the app
│
├── docs/
│     ├── architecture.md/         # how the project is structured
│     ├── expansionideas.md/       # what to implement in future updates
│     └── knownissues.md/          # current concerns and unsolved bugs and errors
│
├── templates/
│     index.html
│
└── README.md                      # Setup instructions
