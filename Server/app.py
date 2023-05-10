from flask import Flask
import os
from flask import Flask, json, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS.
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/repositories', methods=['GET'])
def repositories():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static', 'repositories.json')
    return json.load(open(json_url))

@app.route('/', methods=['GET'])
def welcome():
    return "Server is working...."

@app.errorhandler(404)
def invalid_route(error):
    return jsonify({'errorCode' : 404, 'message' : 'Route not found!'}), 404

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug= True)
