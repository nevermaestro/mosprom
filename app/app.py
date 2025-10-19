import json
import parser
from flask import Flask, render_template, jsonify, abort, make_response, request

app = Flask(__name__)
with open("data/gen.json", mode="r",encoding="utf-8") as json_data_file:
    json_data = json.load(json_data_file)
    
@app.route("/")
def homepage():
    return render_template("index.html",title="FLAME")

# Global orgs endpoints

@app.route("/api/orgs", methods=['GET'])
def get_orgs():
    return jsonify({"orgs":json_data})

@app.route("/api/orgs", methods=['POST'])
def create_org():
    for i in json_data[-1]:
        if i not in request.json and i != 'id':
            abort(400)
    if not request.json:
        abort(400)
    org = {'id': json_data[-1]['id'] + 1}
    org.update({key: request.json[key] for key in json_data[-1] if key != 'id'})
    json_data.append(org)
    return jsonify({"org":org}),201

# Org specific endpoints

@app.route("/api/orgs/<int:org_id>", methods=['DELETE'])
def delete_task(org_id):
    org = list(filter(lambda t: t['id'] == org_id, json_data))
    if len(org) == 0:
        abort(404)
    json_data.remove(org[0])
    return jsonify({"error": "success"})
                 
@app.route("/api/orgs/<int:org_id>", methods=['GET'])
def get_org(org_id):
    org = list(filter(lambda t: t['id'] == org_id, json_data))
    if len(org) == 0:
        abort(404)
    return jsonify({"org": org[0]})

@app.route("/api/orgs/<int:org_id>", methods=['PUT'])
def update_org(org_id):
    org = list(filter(lambda t: t['id'] == org_id, json_data))
    if len(org) == 0:
        abort(404)
    if not request.json:
        abort(400)
    for key in request.json:
        if key not in json_data[-1] or type(request.json[key]) != type(json_data[-1][key]):
            abort(400)
    for key in request.json:
        org[0][key] = request.json.get(key, org[0][key])
    return jsonify({'org': org[0]})

# Parser and json endpoints

@app.route("/api/orgs/refresh", methods=['GET'])
def update_request():
    parser.parse()
    return jsonify({"success": 1})

if __name__ == "__main__":
    app.run(debug=True)
