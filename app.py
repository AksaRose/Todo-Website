from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import path

DB_NAME = "database.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)
# db.init_app(app)

# create a the database if not exist
def create_database(app):
    if not path.exists(DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')

class Todo(db.Model):
    No = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
def __repr__(self) -> str:
    return f"{self.No} - {self.title}"

create_database(app)


@app.route('/')
def hello_world():
   return render_template('index.html')
   
@app.route('/products')
def products():
    return 'this is a product page'

if __name__ == "__main__":
    app.run(debug=True)