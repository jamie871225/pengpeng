from flask import Flask, request, redirect, render_template, session
import os

app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

@app.before_request
def before_request():
    if request.path in ["", "/", "/signin", "/error", "/signout"] or "templates" in request.path:
        return None
    session.permanent=True
    user=session.get("status")

    if user==False:
        return redirect("/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def login():
    account=request.form["account"]
    password=request.form["password"]
    if account=="test" and password=="test":
        session["status"]="Logged In"
        print(session.get('status'))
        return redirect("http://127.0.0.1:3000/member")
    else:
        return redirect("http://127.0.0.1:3000/error")

@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/signout")
def signout():
    session["status"]=False
    print("Logged Out")
    return redirect("http://127.0.0.1:3000")

app.run(port=3000)