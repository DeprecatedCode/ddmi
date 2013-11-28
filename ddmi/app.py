# Distributed Docker Management Interface
# Author: Nate Ferrero

VERSION = (0, 0, 1)

import logging
from flask import Flask, send_file, jsonify
from api import DDMI

# Flask Server
server = Flask(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
server.logger.addHandler(ch)

@server.route('/')
def index():
    return send_file('static/templates/app.html')

@server.route('/api/me')
def api_me():
    return jsonify(me=api.me())

@server.route('/api/servers')
def api_servers():
    return jsonify(servers=api.servers())

@server.route('/api/server/<ddmi_id>/suspend', methods=["POST"])
def api_server_suspend(ddmi_id):
    api.suspend(ddmi_id)
    return jsonify(ok=True)

@server.route('/api/server/<ddmi_id>/resume', methods=["POST"])
def api_server_resume(ddmi_id):
    api.resume(ddmi_id)
    return jsonify(ok=True)

def init():
    global api
    api = DDMI()
    print "DDMI Server ID: " + api.ddmi_id

if __name__ == '__main__':
    print "Starting DDMI in Development Mode"
    init()
    server.run(host='0.0.0.0', port=4244, debug=True)
