from django import forms


class FormLogin(forms.Form):
    UserName = forms.CharField()
    Password = forms.CharField(widget = forms.PasswordInput)    

class KindergardenForm(FormLogin):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    Institution = forms.CharField()
    role = 'Kindergarden'

    def get_role(self):
        return self.role

class ChildForm(FormLogin):
    FirstName = forms.CharField()
    LastName = forms.CharField()
    role = 'Child'
    rating = 0

    def get_role(self):
        return self.role

    def get_rating(self):
        return self.rating

class ChildEditForm(ChildForm):
    Institution = forms.CharField()
    rating = forms.IntegerField()

class SingleForm(forms.Form):
    data = forms.CharField(label = "")

class DoubleForm(forms.Form):
    data1 = forms.CharField(label = "")
    data2 = forms.CharField(label = "")