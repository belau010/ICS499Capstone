from flask import jsonify, request
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
        except Exception as e:
            print(str(e))
        return jsonify(True)