from flask import render_template, flash, redirect, request, session
from flask_app import app
from flask_app.models.truck import Truck
# from flask_app.models.user import User

@app.route('/')
def home_page():
    trucks = Truck.get_all()
    # sender = User.get_sender(data)
    return render_template('homepage.html', trucks = trucks)

@app.route('/locationSearch', methods=['POST'])
def locationSearch():
    data = {
        "origin" : request.form['origin'],
        "destination" : request.form['destination']
    }
    trucks = Truck.get_search_loc(data)
    return render_template('locationSearch.html', trucks = trucks)

@app.route('/productSearch', methods=['POST'])
def productSearch():
    data = {
        "product" : request.form['product']
    }
    trucks = Truck.get_search_prod(data)
    return render_template('productSearch.html', trucks = trucks)

@app.route('/truckSearch', methods=['POST'])
def truckSearch():
    data = {
        "truckNum" : request.form['truckNum']
    }
    trucks = Truck.get_search_truck(data)
    return render_template('truckSearch.html', trucks = trucks)