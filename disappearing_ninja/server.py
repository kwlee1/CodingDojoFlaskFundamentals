from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ninja')
def ninja():
    return render_template('ninja.html')
@app.route('/ninja/<color>')
def colors(color):
    if color == 'blue':
        return render_template('blue.html')
    if color == 'orange':
        return render_template('orange.html')
    if color == 'red':
        return render_template('red.html')
    if color == 'purple':
        return render_template('purple.html')
    else:
        return render_template('notapril.html')
app.run(debug=True)