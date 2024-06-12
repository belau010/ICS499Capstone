
def initializeShiftModel(db):
    class Shift(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        startTime = db.Column(db.DateTime, nullable = False)
        endTime = db.Column(db.DateTime, nullable = False)
        notes = db.Column(db.String(1000), default = "")
        workerId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
        schedulerId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    db.MODELS["Shift"] = Shift