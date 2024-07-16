from flask import Flask, request
from flask_restful import Resource, Api
import pickle
import pandas
from flask_cors import CORS

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
