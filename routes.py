from urllib.request import Request
from app import app
from flask import render_template, request, redirect, send_from_directory
import messages, users, db, answers

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)

@app.route("/message/<int:id>")
def message(id):
    message = answers.get()
    answer= answers.list()
    return render_template("message.html", id=id, message=message, answer=answer)

@app.route("/comment")
def new1():
    return render_template("comment.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    topic = request.form["topic"]
    if messages.send(content, topic):
        return redirect("/")
    else:
        return render_template("error.html", message="Error")

@app.route("/send1", methods=["POST"])
def send1():
    content = request.form["content"]
    topic = request.form["topic"]
    if messages.send1(content, topic):
        return redirect(request.referrer)
    else:
        return render_template("error.html", message="Error")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Unexisting username and password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Error (likely due to already existing username)")

@app.route('/styles/<path:path>')
def send_stylesheet(path): 
    return send_from_directory('styles', path)