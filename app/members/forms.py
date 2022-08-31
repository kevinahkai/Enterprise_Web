from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from members.models import Account

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    #username = forms.CharField()
    #password1 = forms.CharField(widget=forms.PasswordInput())
    #password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('email', 'username', 'department', 'password1', 'password2', 'phone')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email { email } is already in use.")

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username { username } is already in use.")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        try:
            account = Account.objects.get(phone=phone)
        except Exception as e:
            return phone
        raise forms.ValidationError(f"Phone { phone } is already in use.")

class AccountAuthenticationForm(forms.ModelForm):
    email = forms.EmailField(label="Email" )
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "password")