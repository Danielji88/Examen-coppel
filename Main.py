from flask import Flask, request, jsonify
from dotenv import load_dotenv
import Busquedas as search
from gevent.pywsgi import WSGIServer

from functools import wraps
from flask_jwt_extended import JWTManager
import aadus as regis
import os

Main = Flask(__name__)
Main.config["JWT_SECRET_KEY"] = "Una rata vieja"
Main.config["JWT_ALGORITHM"] = "HS256"

jwt = JWTManager(Main)



@Main.route('/searchComics/xpersonaje/<personaje>', methods=['GET'])
def get_comics_by_character(character):
    return search.get_character(character)

@Main.route('/searchComics/xcomic/<comic>', methods=['GET'])
def get_character_by_comics(comic):
    return search.get_comic(comic)

@Main.route('/searchComics', methods=['GET'])
def get_Personajes():
  
    return search.get_Personajes()

@Main.route('/users', methods=['POST'])
def registro():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')   
    token = data.get('token')
    return regis.registro(name, age, token=None)

if __name__ == '__main__':
   
    http_server = WSGIServer(('', 5000), Main)
    http_server.serve_forever()