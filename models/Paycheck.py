from sqlalchemy import func

def initializePaycheckModel(db):
    class Paycheck(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        workerId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
        startDate = db.Column(db.DateTime, nullable = False)
        endDate = db.Column(db.DateTime, nullable = False)
        hours = db.Column(db.Float, nullable = False, default = 0.0)
        total = db.Column(db.Numeric(10, 2), nullable = False)
            
    db.MODELS["Paycheck"] = Paycheck
    