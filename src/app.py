from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/todos', methods=['GET'])
def todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": True }
]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)