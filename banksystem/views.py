from flask import render_template, url_for, redirect, flash
from banksystem import app, db
from banksystem.models import Customer, Transfers

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/customers')
def customers():
    custs = Customer.query.all()
    print(custs)
    return render_template('viewcustomers.html', title='Customers', custs=custs)