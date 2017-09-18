from flask import Flask, render_template, redirect,request,session,flash
app = Flask(__name__)
app.secret_key = "BbBbBbBbIiIiIiIiLlLlLlLl"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if len(request.form['name']) < 1:
        flash("Name cannot be blank!")
        
    elif len(request.form['comment']) < 1:
        flash("Comment cannot be blank!")
        
    elif len(request.form['comment']) > 120:
        flash("Comment cannot exceed 120 characters!")
    else:
        return render_template('result.html', name=request.form['name'], location = request.form['location'], language = request.form['language'], comment = request.form['comment'])
    return redirect('/')

app.run(debug=True)
