from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#only accept POST reqeusts to the route /hello
@app.route("/hello", methods=["POST"])
def hello():
#name variable should be equal to value in name attribute in HTML form
    name = request.form.get("name")
    return render_template("hello.html", name=name)