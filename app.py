##This file should either be named app.py or application.py
##go to this directory and run 'flash run'
##install flask by 'pip install flask'
from flask import Flask, render_template
import datetime

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

#using conditions
@app.route("/condition")
def newYear():
    now = datetime.datetime.now()
    #boolean expression to check if current month and day is 1
    new_year = now.month == 1 and now.day == 1
    return render_template("hello.html", new_year=new_year)

#using loops
@app.route("/loop")
def AliceBob():
    names = ['Alice', 'Bob', 'Charlie', 'David']
    return render_template("hello.html", names=names)

#using links | IMPORTANT
@app.route("/links")
def linking():
    return render_template("another.html")