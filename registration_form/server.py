# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    if len(request.form['fn']) < 1:
        flash("First Name cannot be blank!")
    elif not NAME_REGEX.match(request.form['fn']):
        flash("First and Last Name can only contain letters!")
    if len(request.form['ln']) < 1: 
        flash("Last Name cannot be blank!")
    elif not NAME_REGEX.match(request.form['ln']):
        flash("First and Last Name can only contain letters!")
    if len(request.form['pw']) < 8:
        flash("Password must be at least 8 characters!")
    if request.form['pw'] != request.form['cpw']:
        flash("Password and Password Confirmation do not match!")
    # else if email doesn't match regular expression display an "invalid email address" message
    else:
        flash("Success!")
    return redirect('/')
app.run(debug=True)