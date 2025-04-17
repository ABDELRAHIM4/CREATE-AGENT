from flask import jsonify
import requests
import os

def create_vapi_agent(data):
    url = "https://docs.vapi.ai/api-reference/assistants/create"
    print("VAPI_API_KEY:", os.getenv('VAPI_API_KEY'))  # Log the API key for debugging
    headers = {
        "Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "config": data.get('config', {}),  # Include the config field
        "name": data['agent_name'],
        "voice_id" : data['voice_id'],
        "instructions": data['instructions']
    }
    print("Request URL:", url)  # Log the request URL
    print("Request Headers:", headers)  # Log the request headers
    response = requests.post(url, headers=headers, json=payload)
    try:    
        return response.json(), response.status_code
    except ValueError:
        return {
            "error": "Invalid response from VAPI API",
            "status_code": response.status_code,
            "raw_response": response.text,
            "request_payload": payload  # Log the request payload for debugging
        }, 500
