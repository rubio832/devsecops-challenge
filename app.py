import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, DevSecOps!"})

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "Hello, DevSecOps!"})
    }