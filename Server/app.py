
from flask import Flask, jsonify
from flask_cors import CORS
from proxy import GithubProxy

app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSON_SORT_KEYS'] = False

# Enable CORS.
CORS(app, resources={r'/*': {'origins': '*'}})

proxy = GithubProxy()

@app.route('/repositories', methods=['GET'])
def repositories():
    repositories = proxy.get_data('user/repos')
    return jsonify(repositories)

@app.route('/', methods=['GET'])
def welcome():
    return "Server is working...."

@app.errorhandler(404)
def invalid_route(error):
    return jsonify({'errorCode' : 404, 'message' : 'Route not found!'}), 404

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug= True)
