from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

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


db.create_all()

@app.route('/',methods=["POST","GET"])
def root():
    
    if request.form:
        form = request.form
        
        b = Book(
            rollnumber = form['roll'],
            room = form['room'],
            machine = form['num']
            
        )
        db.session.add(b)
        db.session.commit()
        return redirect('/')
    else:
        machs = Book.query.order_by(Book.id).all()
        for mach in machs:
            if mach.machine == 1:
                mach1 = mach.rollnumber
                room1 = mach.room
            if mach.machine == 2:
                mach2 = mach.rollnumber
                room2 = mach.room
            if mach.machine == 3:
                mach3 = mach.rollnumber
                room3 = mach.room

        
        return render_template('index.html',mach= mach,mach1=mach1,mach2=mach2,mach3=mach3,room1 = room1,room2 = room2,room3 = room3)





if __name__ == '__main__':
    app.run(debug = True)
