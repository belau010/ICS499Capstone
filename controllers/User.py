from flask import jsonify, request, session
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

        hashedPassword = generate_password_hash(password, method='pbkdf2:sha512', salt_length=8)
        try:
            newUser = User(email=email,password=hashedPassword,firstName=firstName,lastName=lastName)
            db.session.add(newUser)
            db.session.commit()
            return jsonify({"success":True,"user":{"id": newUser.id, "email": newUser.email}})
        except Exception as e:
            print(str(e))
            return jsonify({"success":False,"message":str(e)})

    @app.route('/user/logIn', methods = ['POST'])
    def logIn():
        email = request.json.get("email")
        password = request.json.get("password")

        user = User.query.filter_by(email=email).first()
        # if the user exists and the passwords match, save the user to the session
        if user and check_password_hash(user.password, password):
            del user.password
            session["user"] = {"email": user.email, "firstName": user.firstName, "lastName": user.lastName, "password": user.password, "noShowDays": user.noShowDays, "CallOutDays": user.callOutDays, "id": user.id, "payRate": user.payRate}
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
