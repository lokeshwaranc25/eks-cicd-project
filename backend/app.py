from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "backend",
        "message": "EKS CI/CD Backend API is running"
    })

@app.route("/api/info")
def info():
    return jsonify({
        "application": "EKS CI/CD Microservices Project",
        "service": "backend",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "hostname": socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
