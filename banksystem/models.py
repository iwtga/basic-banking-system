from enum import unique
from banksystem import db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    balance = db.Column(db.Float, nullable=False)
    sent = db.relationship('Transfers', backref='sender')
    received = db.relationship('Transfers', backref='receiver')

    def __repr__(self) -> str:
        return f"<Customer: ({self.id}, {self.name}, {self.email}, {self.balance})>"

class Transfers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    sender_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"<Transfer: ({self.sender_id}, {self.receiver_id}, {self.amount})>"