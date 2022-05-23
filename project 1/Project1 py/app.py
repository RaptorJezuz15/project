# save this as app.py
from flask import Flask
from flask_cors import CORS

import Controller.front_controller1 as fc
app = Flask(__name__)


# Establish all the routes handled by Flask
fc.route(app)
cors = CORS(app)


if __name__ == '__main__':
    app.run()
