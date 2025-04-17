from flask import Flask, render_template, request, jsonify
from services.vapi import create_vapi_agent
from services.retell import create_retell_agent
from dotenv import load_dotenv
import os
import requests


app = Flask(__name__)
load_dotenv()

@app.route('/create-agent', methods=['POST'])
def create_agent():
    data = request.get_json()
    print(data)  # Log the incoming data for debugging
    provider = data.get('provider')
    print(provider)  # Log the provider for debugging
    if provider == 'vapi':
        try:
            response, status_code = create_vapi_agent(data)
            print(response)  # Log the response for debugging
            print("Response status code:", status_code)  # Log the status code
            return jsonify(response), status_code
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}, 500
    elif provider == 'retell':
        try:
            response, status_code = create_retell_agent(data)
            return jsonify(response), status_code
        except requests.exceptions.RequestException as e:  
            return {'error': str(e)}, 500
    else:
        return {'error': 'Invalid provider'}, 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
