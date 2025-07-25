# app.py
# Entry point for the Flask application.

from MVC.View.routes import create_app  # Import the function that sets up the Flask app

app = create_app()  # Instantiate the Flask application

if __name__ == "__main__":  
    # Run the Flask development server with debug mode enabled.
    # Debug mode should be disabled in production for security reasons.
    app.run(debug=True)

