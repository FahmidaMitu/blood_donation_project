from django import forms
from django.contrib.auth.models import User
from .models import DonorProfile, BloodRequest

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = ['blood_group', 'phone', 'location', 'last_donation_date', 'availability', 'description']
        widgets = {
            'last_donation_date': forms.DateInput(attrs={'type': 'date'}),
        }

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['patient_name', 'blood_group', 'hospital_name', 'location', 'required_date', 'bags_required', 'contact_number', 'description', 'status']
        widgets = {
            'required_date': forms.DateInput(attrs={'type': 'date'}),
        }