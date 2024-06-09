from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.initialize import initializeModels

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/ics499capstone'
db = SQLAlchemy(app)
db.MODELS = {}

initializeModels(db)

db.MODELS["User"]

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
