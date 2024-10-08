from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
class User_Register_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(User_Register_Form, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )