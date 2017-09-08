from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    if session.has_key('num'):
        session['num'] += 1 
    else:
        session['num'] = 1
    return render_template('index.html')
@app.route('/plus2')
def plustwo():
    session['num'] += 1
    return redirect('/')
@app.route('/reset')
def reset():
    session['num'] = 0
    return redirect('/')
app.run(debug=True)