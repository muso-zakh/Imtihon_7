from django.forms import EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreateForm(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') 