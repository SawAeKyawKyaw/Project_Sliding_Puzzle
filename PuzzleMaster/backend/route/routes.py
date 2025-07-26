# MVC/View/routes.py
# Flask routes and view logic for the puzzle game web app.

from flask import Flask, render_template, request, send_from_directory, redirect, url_for, session
import os
import uuid  # for generating session IDs

# Import model functions
from backend.service.image_service import fetch_puzzle_images
from backend.service.highscore_service import fetch_high_scores, save_game_record


# Temporary in-memory store for active sessions
active_sessions = {}

def create_app():
    """
    Create and configure the Flask application.
    """
    template_dir = os.path.abspath('templates')
    static_dir = os.path.abspath('static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    app.secret_key = "supersecretkey"  # Required for session management

    @app.route("/")
    def index():  # type: ignore
        """Render the homepage."""
        return render_template("index.html")

    @app.route("/puzzle_settings")
    def sliding():  # type: ignore
        """Render the puzzle settings page with available images."""
        images = fetch_puzzle_images()
        return render_template("puzzle_settings.html", images=images)

    @app.route('/puzzle_images/<filename>')
    def puzzle_image(filename:str): # type: ignore
        """Serve puzzle images from the images directory."""
        image_folder = os.path.abspath('images/puzzle_images')
        return send_from_directory(image_folder, filename)

    @app.route("/highscore")
    def highscore():  # type: ignore # default fallback
        """Redirect to default highscore view with difficulty '3x3' and sorting by 'duration'."""
        return redirect(url_for("highscore_filtered", difficulty="3x3", sort="duration"))

    @app.route("/highscore/<difficulty>")
    def highscore_filtered(difficulty):  # type: ignore # main view
        """
        Render highscore page filtered by difficulty and sort order.

        Query parameter:
            sort: Sorting key (default is 'duration').
        """
        sort_by = request.args.get("sort", "duration")
        scores = fetch_high_scores(difficulty=difficulty, sort_by=sort_by) # type: ignore
        return render_template(
            "highscore.html",
            scores=scores,
            default_filter=difficulty,
            default_sort=sort_by
        )

    @app.route("/start_game", methods=["POST"])
    def start_game():  # type: ignore
        """
        Handle start game requests.

        Expects JSON data with:
            - image: Selected image filename
            - grid: Selected grid size/difficulty

        Creates a new game session and redirects to play page.
        """
        data = request.get_json()
        selected_image = data.get("image")
        grid_size = data.get("grid")

        if not selected_image or not grid_size:
            return {"error": "Missing data"}, 400

        session_id = str(uuid.uuid4())
        session["active_session"] = session_id

        active_sessions[session_id] = {
            "image": selected_image,
            "grid": grid_size
        }

        return {"redirect_url": url_for("play", session_id=session_id)}

    @app.route("/play/<session_id>")
    def play(session_id):  # type: ignore
        """
        Render the puzzle play page for an active session.

        Validates the session before rendering.
        """
        if session.get("active_session") != session_id or session_id not in active_sessions: # type: ignore
            return redirect(url_for("index"))

        game_data = active_sessions[session_id] # type: ignore
        image = game_data["image"] # type: ignore
        grid = game_data["grid"] # type: ignore
        session_id = session_id  # type: ignore

        return render_template("puzzle_play.html", session_id=session_id, image=image, grid=grid)
    
    @app.route("/submit_score", methods=["POST"])
    def submit_score():  # type: ignore
        """
        Handle submission of game score data.

        Expects JSON data with:
            - session_id: Active session identifier
            - duration: Game duration in seconds
            - moves: Number of moves made
        """
        data = request.get_json()
        session_id = data.get("session_id")

        if not session_id or session_id not in active_sessions:
            return {"error": "Invalid session"}, 400

        game_data = active_sessions[session_id] # type: ignore
        image = game_data["image"] # type: ignore
        grid = game_data["grid"] # type: ignore

        duration = data.get("duration")
        moves = data.get("moves")

        if duration is None or moves is None:
            return {"error": "Missing data"}, 400

        save_game_record(
            duration=duration,
            moves=moves,
            difficulty=grid, # type: ignore
            image_name=image # type: ignore
        )

        # Clean up session data
        active_sessions.pop(session_id) # type: ignore
        session.pop("active_session", None) # type: ignore

        return {"redirect_url": url_for("highscore")}

    return app
