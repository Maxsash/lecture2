from flask import Flask, render_template, request, session
#more control over session. How they are stored server side
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#can create a global variable
#notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
    #if list is empty
    #list specific to my session
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])