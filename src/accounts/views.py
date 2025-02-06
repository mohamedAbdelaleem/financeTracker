from django.contrib.auth.signals import user_logged_in
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied
from knox.views import LoginView as knoxLoginView
from knox.models import AuthToken
from .serializers import LoginInputSerializer, SignupInputSerializer, UserOutSerializer
from .service import AuthService


class SignupView(APIView):

    def post(self, request):
        serializer = SignupInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = AuthService()
        print(serializer.validated_data)
        user = service.signup(
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password'],
            first_name = serializer.validated_data['first_name'],
            second_name = serializer.validated_data['second_name']
            )
        out_serializer = UserOutSerializer(instance=user)

        return Response(out_serializer.data)


class LoginView(knoxLoginView):
    permission_classes = (AllowAny,)

    def get_post_response_data(self, user, token, instance):
        UserSerializer = self.get_user_serializer_class()

        data = {"expiry": self.format_expiry_datetime(instance.expiry), "token": token}
        if UserSerializer is not None:
            data["user"] = UserSerializer(user).data

        return data

    def post(self, request):
        serializer = LoginInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = AuthService()
        user = service.authenticate(**serializer.validated_data)

        token_ttl = self.get_token_ttl()
        instance, token = AuthToken.objects.create(user, token_ttl)
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        data = self.get_post_response_data(user, token, instance)
        return Response(data)

