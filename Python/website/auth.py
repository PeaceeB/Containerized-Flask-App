from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


# The hash function is to store a password



@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password!", category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user)
            

    
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first() # Filtering user by email. Only one user can have one email attached to them if they exist
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash('Email already exists', category='error') # Flashes a message on the screen to say "Hey, this email already exists" in the database
        elif username_exists:
            flash('Username is already in use', category='error')
        elif password1 != password2:
            flash('Password does not match!', category='error')
        elif len(username) < 2:
            flash('Username is too short! Minimum 3 characters', category='error')
        elif len(password1) < 6:
            flash('Password is too short!, Minimum 6 characters', category='error')
        elif len(email) < 4:
            flash('Email is invalid', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password2, method='sha256')) # sha256 is an encryption method
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!', category='success')
            return redirect(url_for('views.home')) # redirect to the home page





    return render_template("signup.html", user=current_user)

@auth.route("/logout")
@login_required # Only if you're log in, you can view the home page
def logout():
    logout_user()
    return redirect(url_for("views.home"))