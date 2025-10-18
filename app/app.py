import json
import parser
from flask import Flask, render_template, jsonify, abort, make_response

app = Flask(__name__)
with open("data/orgs.json", mode="r",encoding="utf-8") as json_data_file:
    json_data = json.load(json_data_file)
    
@app.route("/")
def homepage():
    return render_template("index.html",title="Web")

@app.route("/api/orgs", methods=['GET'])
def get_orgs():
    return jsonify({"orgs":json_data})

@app.route("/api/orgs/<int:org_id>", methods=['GET'])
def get_org(org_id):
    org = list(filter(lambda t: t['id'] == org_id, json_data))
    if len(org) == 0:
        abort(404)
    return jsonify({"orgs": org[0]})

@app.route("/api/orgs/refresh", methods=['GET'])
def update_request():
    parser.parse()
    return jsonify({"success": 1})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)
