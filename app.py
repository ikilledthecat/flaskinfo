import subprocess
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    bashCommand = "ip -s address"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output
