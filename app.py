import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/")
def index():
    return jsonify(message="Sample app is running", host=socket.gethostname())


@app.get("/api/slots")
def slots():
    # Placeholder data, similar in shape to a clinic booking response
    return jsonify(slots=[
        {"token": 1, "time": "10:00"},
        {"token": 2, "time": "10:10"},
        {"token": 3, "time": "10:20"},
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
