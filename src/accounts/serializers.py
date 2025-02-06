from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class SignupInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    second_name = serializers.CharField()
    password = serializers.CharField()
    confirmed_password = serializers.CharField()

    def validate(self, attrs):
        password = attrs['password']
        confirmed_password = attrs['confirmed_password']
        if password != confirmed_password:
            raise ValidationError("Passwords mismatch")

        return attrs


class LoginInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "second_name",
            "email",
        ]