from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """custom user creation"""

    class Meta(UserCreationForm):
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    """custom user creation"""

    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"
