from flask import render_template, url_for, redirect, flash
from banksystem import app, db
from banksystem.models import Customer, Transfers
from banksystem.forms import TransferForm

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/customers')
def customers():
    custs = Customer.query.all()
    print(custs)
    return render_template('viewcustomers.html', title='Customers', custs=custs)

@app.route('/transfers')
def transfers():
    return render_template('transfers.html', title="Transfers")

@app.route('/users/<int:id>')
def user(id):
    form = TransferForm()
    cust = Customer.query.filter_by(id=id).first()
    if form.validate_on_submit():
        pass
    return render_template('user.html', cust=cust, form=form, title=cust.name)