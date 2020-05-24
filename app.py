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
        mach1=0
        mach2=0
        mach3=0
        
        machs = Book.query.order_by(Book.id).all()
        for mach in machs:
            if mach.machine == 1:
                mach1 = mach
                
            if mach.machine == 2:
                mach2 = mach
                
            if mach.machine == 3:
                mach3 = mach
                

        
        return render_template('index.html',mach1=mach1,mach2=mach2,mach3=mach3)





if __name__ == '__main__':
    app.run(debug = True)
