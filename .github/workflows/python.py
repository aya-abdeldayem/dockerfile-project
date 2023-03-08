from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'web app created by docker file using python image as base'

app.run(host='0.0.0.0', port=81)