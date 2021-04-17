from random import randint

from flask import request, jsonify

from app import app
from app.controller.alpaca_controller import alpaca_controller

@app.route('/')
@app.route('/<age>')
def index(age=None):
    return alpaca_controller.index(age=age)

# TODO: implement profile for each user
@app.route('/profile/<name>')
def profile(name):
    return alpaca_controller.profile(name)

# TODO: implement api
@app.route('/search/<name>', methods=["GET"])
def search(name):
    # data = request.json
    return alpaca_controller.search(name)

@app.route('/create', methods=["POST"])
def create():
    data = request.json
    return alpaca_controller.create(data['name'], data['sex'], data['bio'], data['dName'], data['age'], data['hobbiesList'], data['contactList'])

@app.route('/delete', methods=["DELETE"])
def delete():
    data = request.json
    return alpaca_controller.delete(data)