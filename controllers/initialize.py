from controllers.User import initializeUserController

def initializeControllers(app, db):
    initializeUserController(app, db)