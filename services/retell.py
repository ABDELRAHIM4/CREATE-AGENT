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
    try:
        response = requests.post(url, headers=headers, json=payload)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
