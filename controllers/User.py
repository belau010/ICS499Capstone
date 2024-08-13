from flask import jsonify, request, session
from email_validator import validate_email
from werkzeug.security import generate_password_hash, check_password_hash

def createRootAdmin(app, db):
    with app.app_context():
        User = db.MODELS["User"]
        if User.query.count() == 0:
            hashedPassword = generate_password_hash(
                "password", method='pbkdf2:sha512', salt_length=8)
            rootAdmin = User(email="Admin", firstName="Administrator",
                             lastName="[N/A]", password=hashedPassword, position=db.MODELS["Position"].ADMINISTRATOR)
            db.session.add(rootAdmin)
            db.session.commit()

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
        payRate = request.json.get("payRate")
        position = request.json.get("position")
        forcePasswordChange = request.json.get("forcePasswordChange")
        try:
            #if validate_email(email) and bool(firstName) and bool(lastName) and len(password) >= 8:
            if not validate_email(email):
                return jsonify({"success":False,"message":"Invalid email."})
            if not bool(firstName):
                return jsonify({"success":False,"message":"First name cannot be blank."})
            if not bool(lastName):
                return jsonify({"success":False,"message":"Last name cannot be blank."})
            if len(password) < 8:
                return jsonify({"success":False,"message":"Password must be at least 8 characters."})
            if float(payRate) < 7.25:
                return jsonify({"success":False,"message":"Pay rate must be at least $7.25."})
            hashedPassword = generate_password_hash(password, method='pbkdf2:sha512', salt_length=8)
            newUser = User(email=email,password=hashedPassword,firstName=firstName,lastName=lastName,payRate=payRate,position=position,forcePasswordChange=forcePasswordChange)
            db.session.add(newUser)
            db.session.commit()
            return jsonify({"success":True,"user":{"id": newUser.id, "email": newUser.email}})
            # else:
            #    return jsonify({"success":False,"message": "Invalid entry"})
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
            session["user"] = user.toDict()
            # return a response to the View that the log in was successful as well as some user information
            return jsonify({"success":True,"user": session["user"]})
        else:
            return jsonify({"success":False,"message": "Incorrect Username or Password"})
        
    @app.route('/user/changePassword', methods=['POST'])
    def changePassword():
        newPassword = request.json.get("newPassword")
        if len(newPassword) >= 8:
            user = User.query.filter_by(id=session["user"]["id"]).first()
            if user:
                hashedPassword = generate_password_hash(newPassword, method='pbkdf2:sha512', salt_length=8)
                user.password = hashedPassword
                user.forcePasswordChange = False
                session["user"]["forcePasswordChange"] = False
                db.session.commit()
                return jsonify({"success": True})
            else:
                return jsonify({"success": False, "message": "User not found"})
        else:
            return jsonify({"success": False, "message": "Password must be at least 8 characters"})
        
    @app.route('/user/isLoggedIn', methods = ['GET'])    
    def isLoggedIn():
        if 'user' in session:
            session["user"] = User.query.filter_by(id=session["user"]["id"]).first().toDict()
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
    
    @app.route('/user/update', methods = ['POST'])
    def updateUser():
        if session["user"]["position"] == "ADMINISTRATOR":
            id = request.json.get("id")
            firstName = request.json.get("firstName")
            lastName = request.json.get("lastName")
            payRate = request.json.get("payRate")
            noShowDays = request.json.get("noShowDays")
            callOutDays = request.json.get("callOutDays")
            position = request.json.get("position")
            forcePasswordChange = request.json.get("forcePasswordChange")
            user = User.query.filter_by(id=id).first()
            if user:
                user.firstName = firstName
                user.lastName = lastName
                user.payRate = payRate
                user.noShowDays = noShowDays
                user.callOutDays = callOutDays
                user.position = position
                user.forcePasswordChange = forcePasswordChange
                db.session.commit()
                return jsonify({"success": True})
            else:
                return jsonify({"success": False, "message": "User not found!"})
        else:
            return jsonify({"success": False, "message": "You are not authorized to do this!"})
        
    
    createRootAdmin(app, db)