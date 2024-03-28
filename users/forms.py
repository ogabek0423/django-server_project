from .models import UserProfile
from django import forms
from django.contrib.auth.models import User
from .models import Problems



class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']




    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class UserLoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserProblemForm(forms.Form):
    class Meta:
        model = Problems
        fields = ['first_name', 'email', 'problem_name', 'problem_description']
