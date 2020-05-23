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
        rol = form['roll']
        room = form['room']
        machine = form['num']
        b = Book(
            rollnumber = form['roll'],
            room = form['room'],
            machine = form['num']
            
        )
        db.session.add(b)
        db.session.commit()
        return redirect('/')
    else:
        mach = Book.query.order_by(Book.id.desc()).first()
        
    return render_template('index.html',mach= mach)





if __name__ == '__main__':
    app.run(debug = True)
