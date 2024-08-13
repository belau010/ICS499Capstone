from sqlalchemy import func

def initializeClockModel(db):
    class Clock(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        timeStamp = db.Column(db.DateTime, default = func.now())
        workerId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
        def toDict(self):
            columns = self.__table__.columns.keys()
            result = {column: getattr(self, column) for column in columns}
            return result 
       
    db.MODELS["Clock"] = Clock
    