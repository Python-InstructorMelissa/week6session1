from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.subject import Subject

@app.route('/')
def index():
    return redirect('/subjects/')

@app.route('/subjects/')
def subjects():
    # knowing that I am going to display a table of all the subjects created on the html I call it subjects plural to remind myself multiple entries returned
    print("all subjects from controller file: ", Subject.getAll())
    return render_template('subjects.html', subjects=Subject.getAll())

@app.route('/subjects/new/')
def newSubject():
    return render_template('newSubject.html')

@app.route('/subjects/create/', methods=['POST'])
def createSubject():
    data = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    Subject.save(data)
    print('Saved the Subject: ', data)
    return redirect('/subjects/')

@app.route('/subjects/<int:subject_id>/view/')
def viewSubject(subject_id):
    data = {
        'id': subject_id
    }
    theClasses = Subject.getCohorts(data)
    return render_template('viewSubject.html', subject=Subject.getOne(data), cohorts=theClasses)

@app.route('/subjects/<int:subject_id>/edit/')
def editSubject(subject_id):
    data = {
        'id': subject_id
    }
    return render_template('editSubject.html', subject=Subject.getOne(data))

@app.route('/subjects/<int:subject_id>/update/', methods=['post'])
def updateSubject(subject_id):
    data = {
        'id': subject_id,
        'name': request.form['name'],
        'description': request.form['description']
    }
    Subject.update(data)
    print("you have updated the subject:", data)
    return redirect(f'/subjects/{subject_id}/view/')

@app.route('/subjects/<int:subject_id>/delete/')
def deleteSubject(subject_id):
    data = {
        'id': subject_id
    }
    Subject.delete(data)
    return redirect('/subjects/')