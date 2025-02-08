from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MODEL_URL = "http://localhost:11434/api/generate"

@app.route("/")
def home():
    return "flask is running"

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt')
        
        if not prompt:
            return jsonify({"error": "Missing prompt"}), 400
            
        response = requests.post(
            MODEL_URL,
            json={
                'model': 'deepseek-r1:8b',
                'prompt': prompt,
                'stream': False,
                'options': {
                    'temperature': 0.7,
                    'num_predict': 2048
                }
            },
            timeout=100000 
        )
        
        response.raise_for_status()
        ollama_data = response.json()
        
        return jsonify({
            "response": ollama_data.get("response", "No content generated")
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)