from flask import Flask, redirect, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import Contests

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ---------- Database configuration -----------
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ------- Create Contest -------
@app.route('/api/contest/create', methods=['POST'])
def createContest():
    data = request.get_json()
    
    # checking if name exits in request
    if "name" not in data.keys():
        return jsonify({
            'status':False,
            "messgae" : "name not found"
        }), 400

    # checking if name is empty
    if data['name'] == "":
        return jsonify({
            'status':False,
            'message':'name is empty'
        }), 400
    
    # checking for description
    if "description" not in data.keys():
        return jsonify({
            'status':False,
            "messgae" : "description not found"
        }), 400

    if data['description'] == "":
        return jsonify({
            'status':False,
            'message':'description is empty'
        }), 400
    
    # checking for language
    if "language" not in data.keys():
        return jsonify({
            'status':False,
            "messgae" : "language not found"
        }), 400

    if data['language'] == "":
        return jsonify({
            'status':False,
            'message':'language is empty'
        }), 400 
    if len(data['language'])>3:
        return jsonify({
            'status':False,
            'message':'language code should be less than 3'
        }), 400
    
    # checking for start_date
    if "start_date" not in data.keys():
        return jsonify({
            'status':False,
            "messgae" : "start_date not found"
        }), 400
    
    if data['start_date'] == "":
        return jsonify({
            'status':False,
            'message':'start_date is empty'
        }), 400
    
    # checking for end_date
    if "end_date" not in data.keys():
        return jsonify({
            'status':False,
            "messgae" : "end_date not found"
        }), 400
    
    if data['end_date'] == "":
        return jsonify({
            'status':False,
            'message':'end_date is empty'
        }), 400
    # checking for p_point
    if "p_point" not in data.keys():
        return jsonify({
            'status':False,
            "messgae" : "p_point not found"
        }), 400
    
    if data['p_point'] == "":
        return jsonify({
            'status':False,
            'message':'p_point is empty'
        }), 400
    
    if not data['p_point'].isnumeric():
        return jsonify({
            'status':False,
            'message':'p_point is not an integer'
        }), 400

    # checking for v_point
    if "v_point" not in data.keys():
        return jsonify({
            'status':False,
            "messgae" : "v_point not found"
        }), 400
    
    if data['v_point'] == "":
        return jsonify({
            'status':False,
            'message':'v_point is empty'
        }), 400
    
    if not data['v_point'].isnumeric():
        return jsonify({
            'status':False,
            'message':'v_point is not an integer'
        }), 400

    con = Contests(
        name=data['name'],
        description=data['description'],
        language = data['language'],
        created_by = 'abc',
        start_date = data['start_date'],
        end_date = data['end_date'],
        c_status = True,
        p_point = data['p_point'],
        v_point = data['v_point']
    )

    db.session.add(con)
    db.session.commit()



    return jsonify({
        "status" : True,
        "message" : "Contest Created"
    }),200 

# ------- Index route -------
@app.route('/')
def index():
    return redirect(app.config["APP_REDIRECT_URI"])


if __name__ == "__main__":
    app.run(debug  = True)
