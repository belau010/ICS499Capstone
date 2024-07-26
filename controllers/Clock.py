from flask import jsonify, request, session

def initializeClockController(app, db):
    print("initializing user controller...")
    Clock = db.MODELS["Clock"]

    @app.route('/clock/create', methods = ['POST'])
    def createClock():
        workerId = session["user"]["id"]
        try:
            newClock = Clock(workerId = workerId)
            db.session.add(newClock)
            db.session.commit()
            return jsonify({"success": True})
        except Exception as e:
            print("Error clocking in/out")
            print(e)
            return jsonify({"success": False})
    
    @app.route('/clock/checkWorking', methods = ['GET'])
    def checkWorking():
        count = len(Clock.query.filter_by(workerId = session["user"]["id"]).all())
        return jsonify({"success": count % 2 != 0})