from datetime import datetime
from flask import jsonify, request, session

def initializeShiftController(app, db):
    print("initializing shift controller...")
    Shift = db.MODELS["Shift"]
    User = db.MODELS["User"]

    @app.route('/shift/create', methods = ['POST'])
    def createShift():
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
    def readShiftByUser():
        userId = request.args.get("userId")
        results = Shift.query.filter_by(workerId=userId)
        shifts = []
        for result in results:
            shifts.append(result.toDict())
        return jsonify({"success":True, "shifts":shifts})
    
    @app.route('/shift/update', methods=['POST'])
    def updateShift():
        id = request.json.get("id")
        startTime = request.json.get("startTime")
        endTime = request.json.get("endTime")
        notes = request.json.get("notes")
        shift = Shift.query.filter_by(id=id).first()
        if shift:
            shift.startTime = startTime
            shift.endTime = endTime
            shift.notes = notes
            db.session.commit()
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "The shift could not be found"})
    
    @app.route('/shift/readByDate', methods=['GET'])
    def viewFullSchedule():
        date = datetime.strptime(request.args.get('date'), "%Y-%m-%d")
        results = Shift.query.filter(db.func.date(Shift.startTime) == date.date()).all()
        shifts = []
        for result in results:
            shift = result.toDict()
            shiftWorker = User.query.filter_by(id=shift["workerId"]).first()
            shift["workerFirstName"] = shiftWorker.firstName
            shift["workerLastName"] = shiftWorker.lastName
            shifts.append(shift)
        return jsonify({"success": True, "shifts": shifts})
        