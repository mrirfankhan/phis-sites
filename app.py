from flask import Flask,render_template,redirect,request
from  flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usersdata.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user=User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect("clam")
    return render_template("login.html")


@app.route("/")
def gitt():
    db.create_all()
    return render_template("new.html")

@app.route("/clam")
def clam():
    return render_template("clam.html")



    



