from wtforms import Form, BooleanField, TextField, PasswordField, validators

class AddressForm(Form):
    address = TextField('Address', [validators.Length(min=5, max=200)])
    farmerMarkets = BooleanField('Include Farmers Markets', [validators.Optional()])

