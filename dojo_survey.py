from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    return render_template("forms.html")

@app.route("/submitted",methods=['POST','GET'])
def submitted():
    thename = request.form["name"]
    thelocation = request.form["location"]
    thelanguage=request.form["language"]
    thecomments = request.form["comments"]
    return render_template("submitted.html",name=thename,location=thelocation,language=thelanguage,comments=thecomments)

app.run(debug = True)
