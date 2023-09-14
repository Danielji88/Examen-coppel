from flask import request, jsonify
from flask_jwt_extended import create_access_token
import conexcion as basedatos
import json

def registro(name, age, token=None):

    existing_name = basedatos.db.collection.find_one({'name': name})

    if existing_name:
        return jsonify({'Alerta': 'Usuario agregado con anterioridad'}), 400
    else:
        basedatos.db.collection.insert_one({"name": name, "age": age})
        user_id = basedatos.db.collection.find_one({'name': name})

        access_token = create_access_token(identity=str(user_id))

        basedatos.db.collection.update_one({"name": name}, {"$set":{"token": access_token}})

        user = {}
        user["id"] = str(user_id['_id'])
        user["name"] = name
        user["age"] = age
        user["token"] = access_token
        json_user = json.dumps(user, indent=4)

        return json_user
