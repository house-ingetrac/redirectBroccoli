#Team Hello...
#Tiffany Moi and Alessandro Cauthon
#SoftDev1 pd7
#HW07 -- Do I Know You?
#2017-10-05
from flask import Flask, render_template, request, session
import os
app = Flask(__name__)

app.secret_key = os.urandom(32)

#root route pulls up login template
@app.route("/")
def hi():
    return render_template('login.html', message = "")

#auth checks for the correct username and password
@app.route("/auth", methods = ["POST"])
def process():
    person = request.form["User"] #gets the entered username
    pw = request.form["Pass"] #same for pw
    reqmeth = request.method
    if (person == "KenM"): #checks for correct info
        if (pw == "1234"):  
            session["username"] = person
            return render_template('welcome.html', name = person, method = reqmeth) #if theinfo is good, renders the welcome
        else: #if user was correct but pw incorrect, back to login with message
            return render_template('login.html', message = "Invalid Password")
    else: #if ser incorrect, back to login with message
        return render_template('login.html', message = "Invalid Username")

@app.route("/logout")
def logout(): #ends session and brings back to login with message
    session.pop("username")
    return render_template('login.html', message = "Successfully logged out!")

if __name__ == "__main__":
    app.debug = True
    app.run()
