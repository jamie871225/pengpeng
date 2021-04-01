from flask import Flask, request, redirect, render_template, session, url_for
from flask_cors import CORS
import os
import string
import mysql.connector
from mysql.connector import Error

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Drum871225",
    database="website")

cursorSignin = mydb.cursor(buffered=True)
cursorSignin.execute("SELECT DATABASE();")
cursorSignup = mydb.cursor(buffered=True)
cursorSignup.execute("SELECT DATABASE();")

app=Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

@app.before_request
def before_request():
    if request.path in ["", "/", "/signin", "/error", "/signout", "/register", "/signup"] or "templates" in request.path:
        return None
    session.permanent=True
    user=session.get("status")

    if user==False:
        return redirect("/")

@app.route("/")
def index():
    # name=request.args.get("")
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def login():
    sqlSearchResult=[]
    requestAccount=request.form["account"]
    requestPassword=request.form["password"]
    cursorSignin.execute("select name, username, password from user where username=%s;", (requestAccount,))
    for (name, username, password) in cursorSignin:
        sqlSearchResult.append({
            "name":name,
            "username":username,
            "password":password
        })
    if cursorSignin.rowcount>0:
        if sqlSearchResult[0]["username"]==requestAccount and sqlSearchResult[0]["password"]==requestPassword:
            session["status"]=sqlSearchResult[0]["name"]
            return redirect(url_for("member", name=sqlSearchResult[0]["name"]))
        else:
            # return redirect("http://127.0.0.1:3000/error")
            return redirect(url_for("error", message="帳號或密碼輸入錯誤"))
    else:
        return redirect(url_for("error", message="帳號或密碼輸入錯誤"))

@app.route("/register")
def register():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup():
    sqlSearchResult=[]
    requestAccount=request.form["username"]
    global cur
    cursorSignup.execute("select username from user where username=%s;", (requestAccount,))
    for username in cursorSignup:
        sqlSearchResult.append({
            "username":username
        })
    if cursorSignup.rowcount<=0:
        sql='INSERT INTO user (name, username, password) VALUES (%s, %s, %s);'
        newuser=(request.form["name"], request.form["username"], request.form["password"])
        cursor = mydb.cursor()
        cursor.execute(sql, newuser)
        mydb.commit()
        return render_template("index.html")
    else:
        return redirect(url_for("error", message="帳號已經被註冊"))

@app.route("/member/<name>")
def member(name):
    return render_template("member.html", name=name)

@app.route("/error")
def error():
    errorMessage=request.args.get("message")
    return render_template("error.html", errorMessage=errorMessage)

@app.route("/signout")
def signout():
    session["status"]=False
    print("Logged Out")
    return redirect("http://127.0.0.1:3000/")

app.run(port=3000, debug=True)