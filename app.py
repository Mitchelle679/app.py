#Developer Identification
DEVELOPER_NAME = "Iyamu Irenonsen Mitchelle"
DEVELOPER_MATRIC = "24/13610"
DEVELOPER_DEPARTMENT = "Computer Science"
# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
tasks_db = [
    {"task_id": 1, "task_title": "Setup Project", "is_completed": True}
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks_db})

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        "task_id": len(tasks_db) + 1,
        "task_title": data.get("task_title"),
        "is_completed": False
    }
    tasks_db.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = next((t for t in tasks_db if t["task_id"] == id), None)
    if task:
        task['is_completed'] = True
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks_db
    tasks_db = [t for t in tasks_db if t["task_id"] != id]
    return jsonify({"result": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)