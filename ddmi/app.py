# Distributed Docker Management Interface
# Author: Nate Ferrero

VERSION = (0, 0, 1)

import docker
import logging
from flask import Flask, send_file

server = Flask(__name__)
templates = 'static/templates/'

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
server.logger.addHandler(ch)

@server.route('/')
def index():
    return send_file(templates + 'app.html')

if __name__ == '__main__':
    print "Starting DDMI in Development Mode"
    server.run(host='0.0.0.0', port=4244, debug=True)
