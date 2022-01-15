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
    return render_template('viewcustomers.html', title='Customers', custs=custs)

@app.route('/transfers')
def transfers():
    transfs = Transfers.query.all()
    return render_template('transfers.html', title="Transfers", transfs=transfs)

@app.route('/users/<int:id>', methods=["GET", "POST"])
def user(id):
    form = TransferForm()
    cust = Customer.query.filter_by(id=id).first()
    if form.validate_on_submit():
        print(form.data)
        amount = float(form.data['amount'])
        recipient = form.data['transferto']
        recipient.balance += amount
        cust.balance -= amount
        try:
            transaction = Transfers(sender=cust, receiver=recipient, amount=amount)
            db.session.add(transaction)
            db.session.commit()
            return redirect(url_for('customers'))
        except Exception as e:
            print(e)
            print("Error Occured!")
    return render_template('user.html', cust=cust, form=form, title=cust.name)