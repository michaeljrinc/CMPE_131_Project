from flask import Flask, redirect, url_for, render_template
#redirct and url_for allows redirect from a specific function
#grab an html file and render it as ome page


app = Flask(__name__) #create instance of flask web app

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

if __name__ == "main": #runs the app
    app.run(debug = True) #allows for changes to be seen without restarting the server