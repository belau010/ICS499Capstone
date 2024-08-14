from flask import jsonify, request, session

def initializeClockController(app, db):
    print("initializing clock controller...")
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
    
    @app.route('/clock/readByUser', methods = ['GET'])
    def readClockByUser():
        userId = request.args.get("userId")
        clocks = Clock.query.filter_by(workerId=userId).all()
        clockDicts = []
        for clock in clocks:
            clockDicts.append(clock.toDict())
        return jsonify({"success":True,"clocks": clockDicts})
    
    @app.route('/clock/update', methods = ['POST'])
    def updateClock():
        id = request.json.get("id")
        timeStamp = request.json.get("timeStamp")
        print(timeStamp)
        clock = Clock.query.filter_by(id=id).first()
        if clock:
            clock.timeStamp = timeStamp
            db.session.commit()
            return jsonify({"success":True})
        else :
            return jsonify({"success": False, "message": "The clock in/out was not found."})
        
        