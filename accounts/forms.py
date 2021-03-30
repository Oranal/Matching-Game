from django import forms


class FormLogin(forms.Form):
    UserName = forms.CharField()
    Password = forms.CharField(widget = forms.PasswordInput)    

