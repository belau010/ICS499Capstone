from models.User import initializeUserModel
from models.Clock import initializeClockModel
from models.Paycheck import initializePaycheckModel 
from models.Shift import initializeShiftModel

def initializeModels(db):
    initializeUserModel(db)
    initializeClockModel(db)
    initializePaycheckModel(db)
    initializeShiftModel(db)
