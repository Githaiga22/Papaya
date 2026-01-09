"""
 * @title Papaya Forms Module
 * @author Allan Robinson
 * @notice Form definitions and User model for Papaya lending platform
 * @dev Created: January 9, 2026
 * Includes: BorrowForm, WithdrawForm, PaybackForm, SwapForm, User model
 """

from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms import SelectField, DecimalField, SubmitField, FloatField, SubmitField, RadioField
from wtforms.validators import DataRequired, NumberRange
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "assets.json"), "r") as f:
    assets = json.load(f)

# Convert assets list to the format needed for SelectField choices
asset_choices = [(asset, asset) for asset in assets]

class User(UserMixin):
    def __init__(self, id, username, assets, borrowed_assets):
        self.id = id
        self.username = username
        self.assets = assets
        self.borrowed_assets = borrowed_assets  

    def get_borrowed_assets(self):
        return self.borrowed_assets

class BorrowForm(FlaskForm):
    asset_type = SelectField('Asset Type', choices=asset_choices, validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Borrow')

class WithdrawForm(FlaskForm):
    asset_type = SelectField('Asset Type', choices=asset_choices, validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Withdraw')

class PaybackForm(FlaskForm):
    asset_type = SelectField('Asset Type', choices=asset_choices, validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Payback')

class SwapForm(FlaskForm):
    from_asset = SelectField('From Asset', choices=asset_choices, validators=[DataRequired()])
    to_asset = SelectField('To Asset', choices=asset_choices, validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0.000001)])
    submit = SubmitField('Swap')
