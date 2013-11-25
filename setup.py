import os
from setuptools import setup
from ddmi.app import VERSION

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ddmi",
    version=".".join(map(str, VERSION)),
    author = "Nate Ferrero",
    author_email = "nateferrero@gmail.com",
    description = ("Distributed Docker Management Interface"),
    url='https://github.com/NateFerrero/ddmi',
    license = "MIT",
    packages=['ddmi'],
    install_requires=['flask>=0.10', 'docker-py>=0.2.2'],
    long_description=read('README.md'),
    requires=['flask', 'docker'],
    scripts=['bin/ddmi-server'],
    package_data={
        'ddmi': [
            'static/gumby/fonts/*/*',
            'static/gumby/css/gumby.css',
            'static/angular.min.js',
            'static/ddmi/*',
            'templates/*'
        ]
    }
)
