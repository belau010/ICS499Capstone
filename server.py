from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.initialize import initializeModels
from controllers.initialize import initializeControllers
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"], supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/ics499capstone'
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = "keyboardcat"
Session(app)
db = SQLAlchemy(app)
db.MODELS = {}

initializeModels(db)
initializeControllers(app, db)

db.MODELS["User"]

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
