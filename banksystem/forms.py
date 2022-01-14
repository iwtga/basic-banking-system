from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from banksystem.models import Customer

def choice_query():
    return Customer.query

class TransferForm(FlaskForm):
    tranferto = QuerySelectField(query_factory=choice_query, allow_blank=False, get_label='name')