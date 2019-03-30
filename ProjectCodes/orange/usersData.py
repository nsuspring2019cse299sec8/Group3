from databaseConnection import dataCursor
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class Users:
    pass


class RegistrationForm(Form):
    firstName = StringField('First Name', [
        validators.Length(min=1, max=50),])
    lastName = StringField('Last Name', [
        validators.Length(min=1, max=50)])
    address = StringField('Address', [
        validators.Length(min=1, max=50)])
    emailAddress = StringField('Email Address', [
        validators.Length(min=5, max=50)])
    cellPhone = StringField('Cell Phone Number', [
        validators.Length(min=11, max=11)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=8),
        validators.EqualTo('confirmPassword')])
    confirmPassword = PasswordField('Repeat Password', [
        validators.DataRequired(),
        validators.Length(min=8)])

