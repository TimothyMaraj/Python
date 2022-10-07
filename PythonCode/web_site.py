import flask
""" tasks are to use a production WSGI server
"""
# make sure to run the "venv\Scripts\activate" in path " PS C:\Users\timot\Desktop\Flask\FlaskProject> ""
# then you can run flask --app "name of file minus .py" run 
# enter "deactivate "when leaving the venv

app = flask.Flask(__name__)

@app.route("/")
def home():
    return "<p>My Favorite Things</p><ol><li>EE</li><li>CS</li><li>Food</li><li>Water</li><li>Mi Amor, Mi Alma, Mi Esposa: Vero <3</li></ol>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')