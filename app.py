from flask import Flask, redirect,request,jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import IndexPages

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#---------- Database configuration -----------//
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# ------- Index route -------
@app.route('/')
def index():
    return redirect(app.config["APP_REDIRECT_URI"])

@app.route('/api/index/add',methods=["POST"])
def indexpages():

    data = request.json 

    if not "idpb" in data.keys():
        return jsonify({
            "status" : False,
            "message": "idpb is missing"
        }), 400

    if data["idpb"] == "":
         return jsonify({
            "status" : False,
            "message": "idpb is empty "
        }), 400 
    

    if not "index_name" in data.keys():
        return jsonify({
            "status": False,
            "message": "Index name is missing"
        }),400

    if data["index_name"]== "":
        return jsonify({
            "status": False,
            "message":"Index name is empty"

        }),400


    if not "index_page" in data.keys():
        return jsonify({
            "status": False,
            "message": "Page name is missing"
        })

    if data["index_page"]== "":
        return jsonify({
            "status": False,
            "message": "Page name is empty"
        })
    

    if not "icode" in data.keys():
        return jsonify({
            "status":False,
            "message": "Code is missing"
        }), 400

    if data["icode"]== " ":
        return jsonify({
            "status": False,
            "message": "Code is empty"
        }), 400
    
    
    indexp = IndexPages(
        idpb= data["idpb"],
        index_name = data["index_name"],
        index_page = data["index_page"],
        icode = data["icode"]
    )
    db.session.add(indexp)
    db.session.commit()

    
    return jsonify({
        "staus": True,
        "message": "Sucesfully added"
    }),200


if __name__ == "__main__":
    app.run()
