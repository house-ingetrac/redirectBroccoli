#Team redirectBroccoli
#Alessandro Cartegni, Terry Guan
#SoftDev1 pd7
#HW08 --
#2017-10-06
from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
app = Flask(__name__)

app.secret_key = os.urandom(32)
usr = "KenM"
passw = "1234"
method = ""
#root route pulls up login template
@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("welcome"))
    return render_template("login.html")

@app.route("/welcome")
def welcome():
    if "username" not in session:
        return render_template("login.html",)
    else:
        return render_template("welcome.html", name = usr, method= method)
#auth checks for the correct username and password
@app.route("/auth", methods = ["POST"])
def auth():
    person = request.form["User"] #gets the entered username
    pw = request.form["Pass"] #same for pw
    global method
    method = request.method
    if (person == usr): #checks for correct info
        if (pw == passw):
            session["username"] = person
            return redirect(url_for("welcome"))
        else: #if user was correct but pw incorrect, back to login with message
            flash("Invalid Password")
            # return render_template('login.html', message = "Invalid Password")
    else: #if ser incorrect, back to login with message
        flash("Invalid Username")
        # return render_template('login.html', message = "Invalid Username")
    return render_template("login.html")
@app.route("/logout")
def logout(): #ends session and brings back to login with message
    session.pop("username")
    return redirect(url_for("welcome"))
if __name__ == "__main__":
    app.debug = True
    app.run()
