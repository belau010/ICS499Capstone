from flask import jsonify, request, session
from email_validator import validate_email
from werkzeug.security import generate_password_hash, check_password_hash

def initializeUserController(app, db):
    print("initializing user controller...")
    # this is where controllers will go
    # for example, if the user logs in, it will hit a route with
    # a controller function that is established in thie python file
    User = db.MODELS["User"]

    @app.route('/user/register', methods = ['POST'])
    def register():
        email = request.json.get("email")
        firstName = request.json.get("firstName")
        lastName = request.json.get("lastName")
        password = request.json.get("password")
        try:
            if validate_email(email) and bool(firstName) and bool(lastName) and len(password) >= 8:
                hashedPassword = generate_password_hash(password, method='pbkdf2:sha512', salt_length=8)
                newUser = User(email=email,password=hashedPassword,firstName=firstName,lastName=lastName)
                db.session.add(newUser)
                db.session.commit()
                return jsonify({"success":True,"user":{"id": newUser.id, "email": newUser.email}})
            else:
                return jsonify({"success":False,"message": "Invalid entry"})
        except Exception as e:
            print(str(e))
            return jsonify({"success":False,"message":str(e)})

    @app.route('/user/logIn', methods = ['POST']) 
    # the above line dictates that the below function fires when this API endpoint
    # is hit from the front end (aka the View) using the POST method
    def logIn():
        email = request.json.get("email")
        password = request.json.get("password")
        # we get the data from the HTTP post request for the email and password
        user = User.query.filter_by(email=email).first()
        # if the user exists and the passwords match, save the user to the session
        # instead of having to make an SQL query, we leverage MySQL alchemy to simplify
        if user and check_password_hash(user.password, password):
            session["user"] = {"email": user.email, "firstName": user.firstName, "lastName": user.lastName, "password": user.password, "noShowDays": user.noShowDays, "CallOutDays": user.callOutDays, "id": user.id, "payRate": user.payRate}
            # return a response to the View that the log in was successful as well as some user information
            return jsonify({"success":True,"user": session["user"]})
        else:
            return jsonify({"success":False,"message": "Incorrect Username or Password"})
        
    @app.route('/user/isLoggedIn', methods = ['GET'])    
    def isLoggedIn():
        if 'user' in session:
            return jsonify({"success": True, "user": session["user"]})
        else:
            return jsonify({"success": False})
        
    @app.route('/user/logOut', methods = ['DELETE'])
    def logOut():
        session.pop("user")

        return jsonify({})
    
    @app.route('/user/search', methods = ['GET'])
    def searchUser():
        lastName = request.args.get('lastName')
        users = User.query.filter(User.lastName.like(f'%{lastName}%')).all()
        response = []
        for user in users:
            print("!")
            response.append(user.toDict())
        return jsonify({"success": True, "users": response})