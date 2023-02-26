from flask import Flask, redirect, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import ContestAdmin

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ---------- Database configuration -----------
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# ------- Index route -------
@app.route('/')
def index():
    return redirect(app.config["APP_REDIRECT_URI"])

@app.route('/api/admin/remove', methods=['POST'])
def remove_admin():
    data = request.json

    if not "user_name"in data.keys():
        return jsonify({
            "status": False,
            "message":"Username is not there"
        }), 400
    
    if data["user_name"] == "":
        return jsonify({
            "status": False,
            "message":"Username is empty"
        }), 400


    if not "contest_id" in data.keys():
        return jsonify({
            "status": False,
            "message":"customer_id is not there"
        }), 400
    
    if data["contest_id"] == "":
        return jsonify({
            "status": False,
            "message":"customer_id is empty"
        }), 400
      
    ContestAdmin.query.filter_by(c_id=data["contest_id"], user_name=data["user_name"]).delete()

    return jsonify({
        "status": True,
        "message":"Admin is removed"
    }), 200

if __name__ == "__main__":
    app.run()
