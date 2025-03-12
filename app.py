from flask import Flask, request, jsonify
import requests
from fetch_available_slots import get_available_slots  # Import the function

app = Flask(__name__)

# OpenAI will call this endpoint
@app.route("/openai/get_available_slots", methods=["POST"])
def openai_available_slots():
    data = request.json
    doctor_name = data.get("doctor_name", "")

    if not doctor_name:
        return jsonify({"error": "Missing doctor_name"}), 400

    slots = get_available_slots(doctor_name)
    return jsonify(slots)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


