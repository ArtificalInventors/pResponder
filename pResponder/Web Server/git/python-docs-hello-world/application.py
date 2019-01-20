##from flask import Flask
##app = Flask(__name__)
##
##@app.route("/")
##def hello():
##    return "Hello World!"

from flask import Flask, request
import requests
import json
import shlex
import subprocess

cmd = '''curl -i -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMkQ5VjciLCJzdWIiOiI3OFlDOTciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd3dlaSB3c29jIHdhY3Qgd3NldCB3bG9jIiwiZXhwIjoxNTQ4NTY4OTk4LCJpYXQiOjE1NDc5NjQxOTh9.FZFOy5uPYEh_hRhnIC4rBcFIiLNwrCyDaoxXyrhGbRw' https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1min.json'''
args = shlex.split(cmd)
process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

app = Flask(__name__)

@app.route("/")
def currentPulse():
    return (str(stdout)[-50:-48])
