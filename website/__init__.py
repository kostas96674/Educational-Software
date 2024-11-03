from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the SQLAlchemy object
db = SQLAlchemy()

# Factory function to create the Flask application
def create_app():
    # Create an instance of the Flask class
    app = Flask(__name__)
    
    # Set configuration parameters for the Flask app
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'  # Secret key for session management
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:9667@localhost/python_course'  # Database URI
    
    # Initialize the database object with the app
    db.init_app(app)

    # Import and register the blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import the User model
    from .models import User

    # Create the database tables within the application context
    with app.app_context():
        db.create_all()

    # Initialize the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Set the login view
    login_manager.init_app(app)  # Bind the login manager to the app

    # Define the user loader callback function without this we cannot load our website
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))  # Load the user from the database by ID

    return app
