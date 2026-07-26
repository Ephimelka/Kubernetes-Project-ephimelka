from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "app": "CloudPilot",
        "version": os.environ.get("APP_VERSION", "1.0.0"),
        "hostname": socket.gethostname(),
        "environment": os.environ.get("APP_ENV", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
