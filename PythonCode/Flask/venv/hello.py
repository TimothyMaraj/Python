#https://flask.palletsprojects.com/en/2.2.x/quickstart/
#https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>My Favorite Things</p> <ol> <li>money</li> <li>swag</li> <li>weed</li> </ol>"