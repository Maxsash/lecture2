##This file should either be named app.py or application.py
##go to this directory and run 'flash run'
##install flask by 'pip install flask'
from flask import Flask

#create a new 'Flask' web-application
#__name__ represents current file
app = Flask(__name__)

#flask is designed in terms of routes. Where route is part of URL that you type in
#/ represents the default page
#when user goes to '/' the code immediately below it should run.
#special line called a 'decorator'
@app.route("/")
def index():
    return "Hello, there!!"