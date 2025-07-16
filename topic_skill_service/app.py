# data_manager.py

from flask import Flask, jsonify
from data_manager import JsonDataManager

app = Flask(__name__)
data_manager = JsonDataManager(base_path="data")

@app.route("/")
def hello():
    return "Hello from Topic & Skill Service!"

@app.route("/topics", methods=["GET"])
def get_topics():
    topics = data_manager.read_data("topics.json")
    return jsonify(topics)

@app.route("/skills", methods=["GET"])
def get_skills():
    skills = data_manager.read_data("skills.json")
    return jsonify(skills)

@app.route("/topics/<int:topic_id>", methods=["GET"])
def get_topic_by_id(topic_id):
    topics = data_manager.read_data("topics.json")
    topic = next((t for t in topics if t["id"] == topic_id), None)
    if not topic:
        return jsonify({"error": "Topic not found"}), 404
    return jsonify(topic)

@app.route("/skills/<int:skill_id>", methods=["GET"])
def get_skill_by_id(skill_id):
    skills = data_manager.read_data("skills.json")
    skill = next((s for s in skills if s["id"] == skill_id), None)
    if not skill:
        return jsonify({"error": "Skill not found"}), 404
    return jsonify(skill)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
