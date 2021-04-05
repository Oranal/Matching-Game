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

    def get_role(self):
        return self.role

class ChildForm(forms.Form):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    UserName = forms.CharField()
    Password = forms.CharField(widget = forms.PasswordInput)
    # Institution = forms.CharField()
    role = 'Child'
    rating = 0

    # def __init__(self, institution):
    #     self.Institution = institution
    def get_role(self):
        return self.role

    def get_rating(self):
        return self.rating
