##This file should either be named app.py or application.py
##go to this directory and run 'flash run'
##install flask by 'pip install flask'
from flask import Flask, render_template

#create a new 'Flask' web-application
#__name__ represents current file
app = Flask(__name__)

#flask is designed in terms of routes. Where route is part of URL that you type in
#/ represents the default page
#when user goes to '/' the code immediately below it should run.
#special line called a 'decorator'
@app.route("/")
def index():
    return "Hello, there!!! This is Maxsash."

#adding another route
@app.route("/maxsash")
def maxsash():
    return "What are you doing here??"

#adding a variable
@app.route("/<string:name>")
def hello(name):
    return f"<h1>What are you doing here, {name}??</h1>"

#render_template
#it will only look for hello.html inside the directory 'templates'
@app.route("/index")
def alto():
    return render_template("hello.html")

@app.route("/variable")
def head():
    headline = "Forehead wrinkle is a headline"
    return render_template("hello.html", headline=headline)
#This will set the 'headline' variable inside hello.html equal to headline variable in this function