from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Flask on Kubernetes!",
        "version": "1.0",
        "environment": os.getenv('FLASK_ENV', 'production')
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
