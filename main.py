from flask import Flask, jsonify, request
from dal.FileUtil import FileUtil

import uuid

p_file="./data/products.json"
app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': FileUtil.readFromFile(p_file)})

@app.route('/tasks', methods=['POST'])
def create_task(jsonPayload):
    new_task = {
        'id': uuid.uuid4().hex,
        'title': 'title',
        'description': 'description',
        'completed': False
    }
    tasks = FileUtil.readFromFile(p_file)
    tasks.append(new_task)
    FileUtil.saveToFile(p_file, tasks)
    return jsonify({'task': new_task})



if __name__ == '__main__':
    app.run(debug=True)