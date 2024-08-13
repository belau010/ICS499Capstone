import enum

class Position(enum.Enum):
    ASSOCIATE = "associate"
    MANAGER = "manager"
    ADMINISTRATOR = "administrator"

def initializeUserModel(db):
    class User(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        email = db.Column(db.String(255), unique = True, nullable = False)
        password = db.Column(db.String(255), nullable = False)
        firstName = db.Column(db.String(255), nullable = False)
        lastName = db.Column(db.String(255), nullable = False)
        noShowDays = db.Column(db.Integer, default = 0)
        callOutDays = db.Column(db.Integer, default = 0)
        payRate = db.Column(db.Numeric(10, 2), default = 15.0, nullable = False)
        position = db.Column(db.Enum(Position), default = Position.ASSOCIATE, nullable = False)
        forcePasswordChange = db.Column(db.Boolean, default = True, nullable = False)

        def toDict(self):
            columns = self.__table__.columns.keys()
            result = {column: getattr(self, column) for column in columns}
            result["position"] = self.position.name if self.position else None
            result.pop("password")
            return result 

    db.MODELS["User"] = User
    db.MODELS["Position"] = Position
    
