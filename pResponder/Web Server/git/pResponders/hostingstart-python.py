# from flask import Flask, request
# app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def hello():
#     return "Hello World!reee"

# if __name__ == "__main__":
#     app.run(debug=True)

import sys
import platform

def application(environ, start_response):
    start_response(b'200 OK', [(b'Content-Type', b'text/html')])
    with open ("hostingstart-python.html", "r") as hostingstart_file:
        hosting = hostingstart_file.read()
        yield hosting.encode('utf8').replace(b'PYTHON_VERSION', platform.python_version().encode('utf8'))