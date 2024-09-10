from django import forms
from .models import *


class SudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'course', 'student_time', 'address', 'birthday', 'phone']

    def __init__(self, *args, **kwargs):
        super(SudentForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['amount', 'sale', 'payment_check', 'comment']

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )
