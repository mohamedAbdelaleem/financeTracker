from rest_framework.exceptions import ValidationError
from .models import User


class AuthService:
    
    def signup(self, email: str, password: str, **extra_fields) -> User:
        print(email)
        email_in_use = User.objects.filter(email=email).exists()
        if email_in_use:
            raise ValidationError("Email is in use")
        user = User.objects.create_user(email, password, **extra_fields)
        return user

    def authenticate(self, email: str, password: str) -> User:
        user = User.objects.filter(email=email).first()
        if not user:
            raise ValidationError("Invalid email or password")
        if not user.check_password(password):
            raise ValidationError("Invalid email or password")
        
        return user