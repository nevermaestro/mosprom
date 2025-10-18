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

# FIXME
'''
@app.route("/api/orgs/<int:org_id>", methods=['PUT'])
def update_org(org_id):
    org = list(filter(lambda t: t['id'] == org_id, json_data))
    if len(org) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'ИНН' in request.json and type(request.json['ИНН']) != str:
        abort(400)
    if 'Название' in request.json and type(request.json['Название']) != str:
        abort(400)
    if 'Выручка' in request.json and type(request.json['Выручка']) != int: # hmmmm
        abort(400)
    if 'ОРГН' in request.json and type(request.json['ОРГН']) != str:
        abort(400)
    org[0]['ИНН'] = request.json.get('ИНН', org[0]['ИНН'])
    org[0]['Название'] = request.json.get('Название', org[0]['Название'])
    org[0]['Выручка'] = request.json.get('Выручка', org[0]['Выручка'])
    org[0]['ОГРН'] = request.json.get('ОГРН', org[0]['ОГРН'])
    return jsonify({'error': 'success'})
'''
# Parser and json endpoints

@app.route("/api/orgs/refresh", methods=['GET'])
def update_request():
    parser.parse()
    return jsonify({"success": 1})

if __name__ == "__main__":
    app.run(debug=True)