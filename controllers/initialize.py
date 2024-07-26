from controllers.User import initializeUserController
from controllers.Shift import initializeShiftController
from controllers.Clock import initializeClockController

def initializeControllers(app, db):
    initializeUserController(app, db)
    initializeShiftController(app, db)
    initializeClockController(app, db)