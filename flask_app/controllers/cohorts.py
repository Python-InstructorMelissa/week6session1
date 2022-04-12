from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.cohort import Cohort
from flask_app.models.subject import Subject

# Display all render template
@app.route('/cohorts/')
def cohorts():
    theCohorts = Cohort.getAll()
    theSubjects = Subject.getAll()
    return render_template('cohorts.html', cohorts=theCohorts, subjects=theSubjects)

# display form to create render template
@app.route('/cohorts/new/')
def newCohort():
    theSubjects = Subject.getAll()
    return render_template('newCohort.html', subjects=theSubjects)

# create redirect
@app.route('/cohorts/create/', methods=['post'])
def createCohort():
    data = {
        'name': request.form['name'],
        'instructor': request.form['instructor'],
        'cohortLength': request.form['cohortLength'],
        'subject_id': request.form['subject_id']
    }
    Cohort.save(data)
    print("saved the cohort: ", data)
    return redirect('/cohorts/')

# display one render template
@app.route('/cohorts/<int:cohort_id>/view/')
def viewCohort(cohort_id):
    pass

# edit one render template
@app.route('/cohorts/<int:cohort_id>/edit/')
def editCohort(cohort_id):
    pass

# update one redirect
@app.route('/cohorts/<int:cohort_id>/update/', methods=['post'])
def updateCohort(cohort_id):
    pass

# delete one redirect
@app.route('/cohorts/<int:cohort_id>/delete/')
def deleteCohort(cohort_id):
    pass