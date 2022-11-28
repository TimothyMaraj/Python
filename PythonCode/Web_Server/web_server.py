


"""

TODO: 
- check out here for dynamics 
- https://github.com/Absolute-Tinkerer/Clock-of-Clocks


- Look into templating with {%%} for html templates
- look into 

- https://stackoverflow.com/questions/53111362/fun-clock-streaming-text-with-python-and-flask
- mentions the video streaming in this link  
"""


import os
from datetime import datetime
import random
from flask import Flask, render_template, request, Response
app = Flask(__name__)



@app.route("/home")
def home():
    numone = random.randint(1,20)
    numtwo = random.randint(1,20)
    return render_template('home.html',random_num_one = numone,random_num_two = numtwo)

@app.route("/attemp1")
def attempt():
    return render_template('attempt1.html')


@app.route("/about")
def about():
    return "<h1>Flask is working</h1>"    

@app.route("/EasterEgg")
def easter_egg(): 
    return render_template('EasterEgg.html')

@app.route("/")
@app.route('/time')
def time_feed():
    #now = datetime.now().strftime("%Y.%m.%d|%H:%M:%S")  # return also will work
    return render_template('time.html') 

@app.route('/test/')
def test():
    #now = datetime.now().strftime("%Y.%m.%d|%H:%M:%S")  # return also will work
    return render_template('test.html') 

@app.route('/naruto_image')
def naruto_image(): 
    #none existance here need to import from Flask
    return send_file( "templates/capture.png", mimetype='image/gif')

if __name__=="__main__":
    app.run(host='0.0.0.0')
    app.debug = True

    #port=random.randrange(1,8080,1)




