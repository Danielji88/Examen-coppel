import os
import hashlib
import requests
from flask import request, jsonify
import json

API_URL = "https://gateway.marvel.com:443/v1/public"
PUBLIC_KEY = "942a975a688d1cb72be72ba3f145e2d1"
PRIVATE_KEY = "016a2b51f18818f147ca677b02ffa040ca5217e5"


def get_character(search_param):
    ts = '1'
    hash_value = hashlib.md5(f"{ts}{PRIVATE_KEY}{PUBLIC_KEY}".encode()).hexdigest()
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts,
        'hash': hash_value,
        'name': search_param,
        'orderBy': 'name'
    }

    response = requests.get(f"{API_URL}/characters", params=params)

    if response.status_code == 200:
        data = response.json()
        data = data["data"]["results"]
        character = {}
        character["id"] = data[0]['id']
        character["name"] = data[0]['name']
        character["image"] = data[0]['thumbnail']
        character["apparances"] = data[0]['comics']['available']
        json_character = json.dumps(character, indent=4)
        return json_character
    else:
        return jsonify({'error': 'No se pudo obtener datos del Personaje'}), 500

def get_Personajes():
    ts = '1'
    hash_value = hashlib.md5(f"{ts}{PRIVATE_KEY}{PUBLIC_KEY}".encode()).hexdigest()
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts,
        'hash': hash_value,
        'orderBy': 'name'
    }
   

    response = requests.get("https://gateway.marvel.com:443/v1/public/characters", params=params)

    if response.status_code == 200:
        data = response.json()
        data = data["data"]["results"]
        character = []
        for x in data:
            character.append(dict(id=x["id"], name=x["name"]))
        json_character = json.dumps(character, indent=4)
        return json_character
    else:
        return jsonify({'error': 'No se pudo obtener datos de los Personajes'}), 500


def get_comic(search_param):
    ts = '1'
    hash_value = hashlib.md5(f"{ts}{PRIVATE_KEY}{PUBLIC_KEY}".encode()).hexdigest()
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts,
        'hash': hash_value,
        'title': search_param,
        'orderBy': 'title'
    }

    response = requests.get(f"{API_URL}/comics", params=params)

    if response.status_code == 200:
        data = response.json()
        data = data["data"]["results"]
        comic = {}
        comic["id"] = data[0]['id']
        comic["title"] = data[0]['title']
        comic["image"] = data[0]['thumbnail']
        comic["onSaleDate "] = data[0]['dates'][0]
        json_character = json.dumps(comic, indent=4)
        return json_character
    else:
        return jsonify({'error': 'No se pudo obtener datos del Comic'}), 500