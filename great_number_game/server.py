from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    print session['num']
    if session.has_key('num'):
        session['num'] = session['num']
    else:
        session['num'] = random.randrange(0,101)
    if session.has_key('hint'):
        hint = session['hint']
    else:
        hint = 'none'
    return render_template('index.html', hint=hint)
@app.route('/submit', methods=['POST'])
def submit():
    guess = int(request.form['myguess'])
    print guess
    if guess > session['num']:
        session['hint'] = "high"
    if guess < session['num']:
        session['hint'] = "low"
    if guess == session['num']:
        session['hint'] = 'yes'
    return redirect('/')
@app.route('/reset')
def reset():
    session['hint'] = 'none'
    session['num'] = random.randrange(0,101)
    print session['num']
    return redirect('/')
app.run(debug=True)