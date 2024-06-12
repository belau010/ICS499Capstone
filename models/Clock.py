from sqlalchemy import func

def initializeClockModel(db):
    class Clock(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        timeStamp = db.Column(db.DateTime, default = func.now())
        workerId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
       
    db.MODELS["Clock"] = Clock
    