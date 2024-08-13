from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from models.initialize import initializeModels
from controllers.initialize import initializeControllers
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "localhost:5173"], supports_credentials=True)
# server connects to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/ics499capstone'
# session settings
app.config["SESSION_PERMANENT"] = True 
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = "keyboardcat"
# session middleware is created 
Session(app)

db = SQLAlchemy(app)
db.MODELS = {}

initializeModels(db)

@app.route("/")
def base():
    return send_from_directory('dist', 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory('dist', path)

if __name__=='__main__':
    with app.app_context():
        db.create_all()
        initializeControllers(app, db)
    app.run(debug=True)
