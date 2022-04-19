from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Register(UserCreationForm):
    email = forms.EmailField(label = "Email", required = True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update(placeholder = self.fields[str(field)].label)
            self.fields[str(field)].label = ""