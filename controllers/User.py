def initializeUserController():
    print("initializing user controller...")
    # this is where controllers will go
    # for example, if the user logs in, it will hit a route with
    # a controller function that is established in thie python file

    @app.route('/user/login', methods = ['POST'])
    def logIn():
        print("log in attempt!")