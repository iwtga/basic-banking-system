from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from banksystem.models import Customer
from wtforms import StringField
from wtforms.validators import DataRequired

def choice_query():
    return Customer.query

class TransferForm(FlaskForm):
    tranferto = QuerySelectField(query_factory=choice_query, allow_blank=False, get_label='name')
    amount = StringField('Amount', validators=[DataRequired()])
