from flask import jsonify
import requests
import os

def create_vapi_agent(data):
    url = "https://docs.vapi.ai/api-reference/assistants/create"
    headers = {
        "Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}",
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
        return {
