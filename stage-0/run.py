from flask import Flask, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/me")
def hello_world():
    current_local_time = datetime.now()
    iso_format_local = current_local_time.isoformat()
    cat_api_endpoint = "https://catfact.ninja/fact"
    
    response = requests.get(cat_api_endpoint);
    data = {
        "status" : "success",
        "user" : {
        "email" : "oyinbunuaatani@gmail.com",
        
        "name" : "Atani Oyinbunua",
        
        "stack" : "Python/Flask",
        },
        "timestamp" : iso_format_local,
        "fact" : response.json()['fact'],
        
    }
    return jsonify(data)
