from flask import Flask, redirect, url_for, render_template, request, session
#redirct and url_for allows redirect from a specific function
#grab an html file and render it as ome page


app = Flask(__name__) #create instance of flask web app
app.secret_key = "password"


#define how to access the certain page
#@app.route("/") #default will go to home page. can define certain
                #pages after '/'


"""
#define the web pages on the website
def home(): #returns what is being displayed on the page using basic text
    
    return "I am stealing KK's job :) <h1>Chicken Nuggets/<h1>" #inline html
"""

@app.route("/", methods=['GET','POST'])
def home(): #returns what is being displayed on the page using html file
    return render_template("home.html") #inline html

@app.route("/login",methods = ['GET','POST'])
def login():
    if request.method == "POST": #will post the information to user
        user = request.form["nm"] #nm is the dictionary and gets it from HTML file
        
        #stores session values
        session["user"] = user
        return redirect(url_for("user"))  
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    #gets user session and checks if it exist
    if "user" in session:
        user = session["user"]
        return render_template("profile.html",user)

    else: 

        #if already logged in, redirect to user page
        if "user" in session:
            return redirect(url_for("user"))
        #will return to login if not found
        return redirect(url_for("login"))


@app.route("/admin") #example of redirect
def admin():
    return redirect(url_for("user", name = "Admin")) #passes name to user() function

@app.route("/noodle")
def noodle():
    return render_template("noodle.html")

@app.route("/pillow")
def pillow():
    return render_template("pillow.html")
'''
@app.route("/<name>") #will pass this as a parameter to the function
def user(name):
    return name + " is ugly too"
'''

@app.route("/logout")
def logout():
    session.pop("user", None) #remove user from session
    return redirect(url_for("login"))

if __name__ == "main": #runs the app
    app.run(debug = True) #allows for changes to be seen without restarting the server