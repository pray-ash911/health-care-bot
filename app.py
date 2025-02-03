from flask import Flask
from route.medication_routes import medication_bp  # Import the medication blueprint

def create_app():
    """
    Application factory to create the Flask app.
    """
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(medication_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
