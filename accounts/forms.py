from django import forms


class FormLogin(forms.Form):
    UserName = forms.CharField()
    Password = forms.CharField(widget = forms.PasswordInput)    

class KindergardenForm(forms.Form):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    UserName = forms.CharField()
    Password = forms.CharField(widget = forms.PasswordInput)
    Institution = forms.CharField()
    role = 'Kindergarden'

