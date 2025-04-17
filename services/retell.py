from flask import jsonify
import requests
import os

def create_retell_agent(data):
    url = "https://docs.retellai.com/api-references/create-agent"
    headers = {
        "Authorization": f"Bearer {os.getenv('RETELL_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": data['agent_name'],
        "voice_id" : data['voice_id'],
        "instructions": data['instructions']
    }
    response = requests.post(url, headers=headers, json=payload)
    try:    
        return response.json(), response.status_code
    except ValueError:
        return {"error": "Invalid response from Retell API"}, 500
