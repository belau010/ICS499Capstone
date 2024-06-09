import enum

class Position(enum.Enum):
    ASSOCIATE = "associate"
    MANAGER = "manager"

def initializeUserModel(db):
    class User(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        email = db.Column(db.String(255), unique = True, nullable = False)
        password = db.Column(db.String(255), nullable = False)
        firstName = db.Colum(db.String(255), nullable = False)
        lastName = db.Colum(db.String(255), nullable = False)
        noShowDays = db.Column(db.Integer, default = 0)
        callOutDays = db.Column(db.Integer, default = 0)
        payRate = db.Column(db.Numeric(10, 2), nullable = False)
        position = db.Column(db.Enum(Position), default = Position.ASSOCIATE, nullable = False)

    db.MODELS["User"] = User
    