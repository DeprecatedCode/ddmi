# Distributed Docker Management Interface
# Author: Nate Ferrero

VERSION = (0, 0, 1)

import docker
from flask import Flask
server = Flask(__name__)

@server.route('/')
def index():
    return 'Hello World!'