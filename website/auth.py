from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db  # Import the database object from the __init__.py file
from flask_login import login_user, login_required, logout_user, current_user
import hashlib

# Define the authentication blueprint
auth = Blueprint('auth', __name__)

# Function to generate a hashed password
def generate_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if the provided password matches the stored hashed password
def check_hash(stored_password, provided_password):
    return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()

# Route for the login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get email and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Query the database for a user with the provided email
        user = User.query.filter_by(email=email).first()
        if user:
            # Check if the provided password matches the stored password
            if check_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)  # Log in the user
                return redirect(url_for('views.home'))  # Redirect to the home page
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    # Render the login template
    return render_template("login.html", user=current_user)

# Route for logging out
@auth.route('/logout')
@login_required
def logout():
    logout_user()  # Log out the user
    return redirect(url_for('auth.login'))  # Redirect to the login page

# Route for the sign-up page
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Get form data
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Validate the form data
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Create a new user
            hashed_password = generate_hash(password1)
            new_user = User(email=email, username=username, password=hashed_password)
            db.session.add(new_user)  # Add the new user to the database
            db.session.commit()
            login_user(new_user, remember=True)  # Log in the new user
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))  # Redirect to the home page

    # Render the sign-up template
    return render_template("sign_up.html", user=current_user)
