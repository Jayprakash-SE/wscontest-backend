from flask import Flask, redirect , request , jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import IndexPages

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ---------- Database configuration -----------
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# ------- Index route -------
@app.route('/')
def index():
    return redirect(app.config["APP_REDIRECT_URI"])

@app.route('/api/index/remove', methods=["POST"])
def indexpage_remove():
    data = request.json 

    if not "idpd" in data.keys():
        return jsonify({
            "status": False,
            "message": "It doesn't exist"
        }), 400
    
    if "idpd" == "":
        return jsonify({
            "status": False,
            "message": "It is empty"
        }), 400
    
    IndexPages.query.filter_by(idpb=data["idpb"]).delete()

    return jsonify({
        "status": True,
        "message": "Sucessfuly removed"
    }), 200

if __name__ == "__main__":
    app.run()
