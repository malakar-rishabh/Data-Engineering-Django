from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signupform(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    user_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    confirm_password = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    phone_number = forms.CharField(max_length=10)
    company_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'user_name', 'password',
                  'confirm_password', 'email', 'phone_number', 'company_name')

    def save(self, commit=True):
        user = super(signupform, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_name = self.cleaned_data['user_name']
        user.password = self.cleaned_data['password']
        user.confirm_password = self.cleaned_data['confirm_password']
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.company_name = self.cleaned_data['company_name']

        if commit:
            user.save()
        return user
