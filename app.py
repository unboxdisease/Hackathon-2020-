from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///machine.db'
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    rollnumber = db.Column(db.Integer, nullable = False)
    room = db.Column(db.Integer, nullable = False)
    machine = db.Column(db.Integer, nullable = False)
    time = db.Column(db.DateTime,default = datetime.utcnow)


db.create_all()

@app.route('/',methods=["POST","GET"])
def root():
    machi = [0,0,0]
    now = datetime.utcnow()
    machs = Book.query.order_by(Book.id).all()
    for mach in machs:
        if mach.machine == 1:
            machi[0] = mach
            
        if mach.machine == 2:
            machi[1] = mach
            
        if mach.machine == 3:
            machi[2] = mach
    if request.form:
        form = request.form
        
        b = Book(
            rollnumber = form['roll'],
            room = form['room'],
            machine = form['num']
            
        )
        if (now - machi[int(form['num']) - 1].time).seconds/60 < 50:

        # if (now - machi[int(form['num']) - 1].time).seconds < 2400:
            return redirect (url_for('error'))
        db.session.add(b)
        db.session.commit()
        return redirect('/')
    else:
        
        mach1=0
        mach2=0
        mach3=0
        
        machs = Book.query.order_by(Book.id).all()
        for mach in machs:
            if mach.machine == 1:
                machi[0] = mach
                
            if mach.machine == 2:
                machi[1] = mach
                
            if mach.machine == 3:
                machi[2] = mach
        

        return render_template('index.html',mach1=machi[0],mach2=machi[1],mach3=machi[2],now=now)
@app.route("/error",methods=["GET"])
def error():
    machi = [0,0,0]
    now = datetime.utcnow()
    machs = Book.query.order_by(Book.id).all()
    for mach in machs:
        if mach.machine == 1:
            machi[0] = mach
            
        if mach.machine == 2:
            machi[1] = mach
            
        if mach.machine == 3:
            machi[2] = mach
    return render_template("error.html",mach1=machi[0],mach2=machi[1],mach3=machi[2],now=now)





if __name__ == '__main__':
    app.run(debug = True)
