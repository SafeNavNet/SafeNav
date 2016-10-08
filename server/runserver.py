"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from flask import Flask, request, jsonify

app = Flask(__name__)





@app.route('/coordinate/<lat1>,<long1>;<lat2>,<long2>')

def show_user_profile(lat1, long1, lat2, long2):

    # show the user profile for that user

    newDict = {}

 
    newDict['lat1'] = lat1

    newDict['long1'] = long1

    newDict['lat2'] = lat2

    newDict['long2'] = long2


    return jsonify(**newDict)


@app.route('/post/<int:post_id>')

def show_post(post_id):

    # show the post with the given id, the id is an integer

    return 'Post %d' % post_id

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
