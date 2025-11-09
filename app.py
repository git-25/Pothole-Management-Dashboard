from flask import Flask, render_template, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

api_key = os.getenv("KAKAO_API_KEY")

pothole_data = [
    {"id": "p1", "latitude": 37.756185, "longitude": 126.768615, "severity": "High", "status": "Resolved"},
    {"id": "p2", "latitude": 37.751426, "longitude": 126.750812, "severity": "Low", "status": "Unresolved"},
    {"id": "p3", "latitude": 37.732988, "longitude": 126.735041, "severity": "Medium", "status": "Resolved"},
    {"id": "p4", "latitude": 37.718336, "longitude": 126.763476, "severity": "Low", "status": "Unresolved"},
    {"id": "p5", "latitude": 37.766131, "longitude": 126.795347, "severity": "High", "status": "Unresolved"},
    {"id": "p6", "latitude": 37.746076, "longitude": 126.800266, "severity": "Medium", "status": "Resolved"},
    {"id": "p7", "latitude": 37.870886, "longitude": 126.787956, "severity": "High", "status": "Resolved"},
    {"id": "p8", "latitude": 37.880694, "longitude": 126.792158, "severity": "High", "status": "Resolved"},
    {"id": "p9", "latitude": 37.862573, "longitude": 126.806002, "severity": "Medium", "status": "Unresolved"},
    {"id": "p10", "latitude": 37.882585, "longitude": 126.771994, "severity": "Medium", "status": "Resolved"},
    {"id": "p11", "latitude": 37.879059, "longitude": 126.758426, "severity": "High", "status": "Resolved"},
    {"id": "p12", "latitude": 37.864601, "longitude": 126.818217, "severity": "Low", "status": "Unresolved"},
    {"id": "p13", "latitude": 37.747332, "longitude": 126.801873, "severity": "Medium", "status": "Resolved"},
    {"id": "p14", "latitude": 37.911007, "longitude": 126.830288, "severity": "High", "status": "Unresolved"},
    {"id": "p15", "latitude": 37.897505, "longitude": 126.823803, "severity": "Medium", "status": "Resolved"},
    {"id": "p16", "latitude": 37.846801, "longitude": 126.859342, "severity": "Medium", "status": "Resolved"},
    {"id": "p17", "latitude": 37.739336, "longitude": 126.824776, "severity": "Low", "status": "Resolved"},
    {"id": "p18", "latitude": 37.846906, "longitude": 126.859267, "severity": "High", "status": "Resolved"},
    {"id": "p19", "latitude": 37.847182, "longitude": 126.869476, "severity": "High", "status": "Unresolved"},
    {"id": "p20", "latitude": 37.818751, "longitude": 126.734887, "severity": "Medium", "status": "Resolved"},
    {"id": "p21", "latitude": 37.816761, "longitude": 126.712833, "severity": "Low", "status": "Resolved"},
    {"id": "p22", "latitude": 37.816118, "longitude": 126.697428, "severity": "High", "status": "Resolved"},
    {"id": "p23", "latitude": 37.828790, "longitude": 126.708313, "severity": "Low", "status": "Unresolved"},
    {"id": "p24", "latitude": 37.817385, "longitude": 126.688992, "severity": "Medium", "status": "Resolved"},
    {"id": "p25", "latitude": 37.771932, "longitude": 126.733582, "severity": "Low", "status": "Resolved"},
    {"id": "p26", "latitude": 37.767003, "longitude": 126.698457, "severity": "Medium", "status": "Resolved"},
    {"id": "p27", "latitude": 37.763906, "longitude": 126.711760, "severity": "Low", "status": "Unresolved"},
    {"id": "p28", "latitude": 37.814455, "longitude": 126.799914, "severity": "High", "status": "Resolved"},
    {"id": "p29", "latitude": 37.819749, "longitude": 126.827768, "severity": "Low", "status": "Unresolved"},
    {"id": "p30", "latitude": 37.846628, "longitude": 126.880324, "severity": "Medium", "status": "Unresolved"},
]

for i, p in enumerate(pothole_data):
    p["timestamp"] = datetime.now().isoformat()
    p["image_url"] = f"https://placehold.co/100x100?text=P{i+1}"

@app.route('/')
def dashboard():
    return render_template('dashboard.html', api_key=api_key)

@app.route('/api/potholes', methods=['GET'])
def get_potholes():
    return jsonify(pothole_data)

@app.route('/api/potholes', methods=['POST'])
def add_pothole():
    data = request.get_json()
    pothole_data.append(data)
    print(f"[NEW DATA] {data}")
    return jsonify({"message": "Pothole added successfully"}), 201

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
