from flask import jsonify, request, session

def initializeShiftController(app, db):
    print("initializing user controller...")
    Shift = db.MODELS["Shift"]

    @app.route('/shift/create', methods = ['POST'])
    def create():
        workerId = request.json.get("workerId")
        startTime = request.json.get("startTime")
        endTIme = request.json.get("endTime")
        notes = request.json.get("notes")
        try:
            newShift = Shift(workerId = workerId, startTime = startTime, endTime = endTIme, notes = notes, schedulerId = session["user"]["id"])
            db.session.add(newShift)
            db.session.commit()
            return jsonify({"success":True,})
        except Exception as e:
            print(str(e))
            return jsonify({"success":False,"message":str(e)})
        
    @app.route('/shift/readByUser', methods = ['GET'])
    def readByUser():
        userId = request.args.get("userId")
        results = Shift.query.filter_by(workerId=userId)
        shifts = []
        for result in results:
            shifts.append(result.toDict())
        return jsonify({"success":True, "shifts":shifts})