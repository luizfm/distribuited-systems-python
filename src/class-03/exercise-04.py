from flask import Flask, jsonify, request

app = Flask(__name__)
names = []

@app.route('/names', methods=['GET', 'POST', 'DELETE'])
def manage_names():
    if request.method == 'GET':
        return jsonify(names)
    elif request.method == 'POST':
        name = request.json.get('name')
        names.append(name)
        return jsonify({ "status": "added", "name": name })
    elif request.method == 'DELETE':
        name = request.json.get('name')
        names.remove(name)
        return jsonify({ "status": "removed", "name": name })
    
app.run()