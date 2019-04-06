from databaseConnection import database
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


class RegisterUser(object):
    def __init__(self, form):
        self.firstName = form.firstName.data
        self.lastName = form.lastName.data
        self.address = form.address.data
        self.emailAddress = form.emailAddress.data
        self.cellPhone = form.cellPhone.data
        self.password = form.password.data

    def store_record(self):
        data_cursor = database.connect()
        sql = "INSERT INTO user_details " \
              "(userID,password,firstName,lastName,address,cellPhoneNumber,emailAddress,status)" \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (self.cellPhone, self.firstName, self.lastName, self.address,
                  self.emailAddress, self.cellPhone, self.password, "active")
        data_cursor.execute(sql, values)
        database.commit()
        data_cursor.close()


class RegistrationForm(Form):
    firstName = StringField('First Name', [
        validators.Length(min=1, max=50)])
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
