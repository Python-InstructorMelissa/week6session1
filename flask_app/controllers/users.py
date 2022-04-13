from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/', methods=['post'])
def register():
    isValid = User.validate(request.form)
    if not isValid: # if isValid = False the redirect as this statement will run
        return redirect('/')
    newUser = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(newUser)
    if not id:
        flash('Something got messed up somewhere')
        return redirect('/')
    session['user_id'] = id
    flash("You are now logged in")
    return redirect('/subjects/')