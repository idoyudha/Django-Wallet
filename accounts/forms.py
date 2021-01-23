from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 



class RecordForm(forms.Form):
    type            = forms.CharField(max_length=40)
    category        = forms.CharField(max_length=40)
    sub_category    = forms.CharField(max_length=40)
    payment         = forms.CharField(max_length=40)
    amount          = forms.FloatField()
    date            = forms.DateField()
    time            = forms.TimeInput()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
