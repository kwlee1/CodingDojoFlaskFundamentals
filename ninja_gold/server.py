from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
    # whatever needs to be appended needs to be added into a list and then use {%for %} to run loop in HTML
    # if session.has_key('app'):
    #     app = session['app']
    # else:
    #     session['app'] = ''
    #     app = session['app']
    if session.has_key('rand'):
        rand = session['rand']
        print rand 
    else:
        session['rand'] = 0
        rand = 0
    if session.has_key('build'):
        build = session['build']
        print build 
    else:
        build = 'none'
    return render_template('index.html',build=build,rand=rand,app=app)
@app.route('/process_money', methods=['POST'])
def submit():
    if session.has_key('rand'):
        session['build'] = request.form['building']
        if session['build'] == 'farm':
            print session['build']
            session['rand'] = random.randrange(10,21)
            mynum = session['rand']
            print session['rand']
        if session['build'] == 'cave':
            print session['build']
            session['rand'] = random.randrange(5,11)
            print session['rand']
        if session['build'] == 'house':
            print session['build']
            session['rand'] = random.randrange(2,6)
            print session['rand']
        if session['build'] == 'casino':
            print session['build']
            session['rand'] = random.randrange(-50,51)
            print session['rand']
        print session['build']
    return redirect('/')
app.run(debug=True)