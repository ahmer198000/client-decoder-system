from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize the app, database, and migration
app = Flask(__name__, static_folder='static')
#app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789abcdefg'  # Change this to a secure random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration system
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize the login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Define login view for unauthorized users

# user_loader function for Flask-Login
from app.models import User  # Ensure to import the User model

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import routes after initializing app
from app import routes
