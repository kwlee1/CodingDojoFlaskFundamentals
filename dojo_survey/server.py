from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def process():
    name = request.form['name']
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(request.form['comment']) < 1:
        flash("Are you sure you want to leave this blank?")
        return redirect('/')
    if len(request.form['comment']) >120: 
        flash("Please limit comment to 120 characters or fewer")
        return redirect('/')
    return render_template('result.html',name = name,location = location,language = language,comment = comment)
app.run(debug=True)