from django import forms
from .models import *


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'profession', 'image', 'phone', 'address']

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )

