from django import forms

from .models import topsis_data


class topsis_form(forms.ModelForm):
    class Meta:
        model = topsis_data
        fields = ('dataset', 'weights', 'impacts', 'email')
