from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {          1: {"title" :"this is my first task" ,
                 "description": "need to finih ny rest project"},
                   2: {"title":"this is second task",  "description": "need finish sql project"
                      }
        }

MAX_ID = len(tasks)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks" : tasks}), 200


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_tasks_id(task_id):
    if task_id in tasks:
        return jsonify(tasks[MAX_ID]), 200
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>/complited", methods=["GET"])
def get_tasks_complited(task_id):
    if task_id in tasks:
        tasks[task_id]["complited"] = True
        return jsonify(tasks[MAX_ID]), 200
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks", methods=["POST"])
def add_task():
    global MAX_ID
    data = request.get_json()
    if not data or "title" not in data or "description" not in data:
       return jsonify({"Error": "Bad Request, data must include 'title' and 'description'"}), 400
    MAX_ID += 1
    tasks[MAX_ID] = {"title": data["title"],
                    "description": data["description"],
                    "complited": False
                    }
    return jsonify(tasks[MAX_ID]), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id in tasks:
       del tasks[task_id]
    return jsonify({"message": "Task is deleted"}), 200


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    if task_id in tasks:
        tasks[task_id] = request.get_json()
        tasks[task_id]["complited"] = False
        return jsonify(tasks[task_id]), 200
    
    return jsonify({"error": "Task is  not found"}), 404   

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050)