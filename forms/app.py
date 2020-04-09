from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#only accept POST reqeusts to the route /hello
#if try to directly access, we get "Method not allowed (GET is not allowed)"
# @app.route("/hello", methods=["POST"])

#accept GET request or POST requests
@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead"
#name variable should be equal to value in name attribute in HTML form
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)