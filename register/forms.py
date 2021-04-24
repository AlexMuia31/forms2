from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from.models import patient


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class patientform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(patientform, self).__init__(*args, **kwargs)
        self.fields['patient_name'].widget.attrs['placeholder'] = 'Enter patient name'
        self.fields['Age'].widget.attrs['placeholder'] = 'Enter patient age'
        self.fields['spirometry_measure'].widget.attrs['placeholder'] = 'Enter FEV1/FVC ratio'
        self.fields['blood_eosinophilis_count'].widget.attrs['placeholder'] = 'Enter blood eosinophils count (%)'

    class Meta:
        model = patient
        fields = "__all__"
