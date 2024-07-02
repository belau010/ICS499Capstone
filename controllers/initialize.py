from controllers.User import initializeUserController
from controllers.Shift import initializeShiftController

def initializeControllers(app, db):
    initializeUserController(app, db)
    initializeShiftController(app, db)