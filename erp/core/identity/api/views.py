from django.contrib.auth import authenticate, login, logout
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from erp.core.identity.api.serializers import (
    LoginResponseSerializer,
    LoginSerializer,
    UserMeSerializer,
)
from erp.core.identity.models import User
from erp.common.api.responses import envelope, error_envelope


def _login_payload(user: User, token: str) -> dict:
    base = UserMeSerializer(user).data
    return {"token": token, **base}


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @extend_schema(
        tags=["auth"],
        request=LoginSerializer,
        responses={200: LoginResponseSerializer},
        examples=[
            OpenApiExample(
                "Demo owner",
                value={"email": "owner@demo.local", "password": "demo1234"},
                request_only=True,
            ),
        ],
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )
        if user is None:
            return error_envelope(
                "authentication_required",
                "Invalid email or password.",
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if not user.is_active:
            return error_envelope(
                "authentication_required",
                "Account is inactive.",
                status=status.HTTP_401_UNAUTHORIZED,
            )
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return envelope(_login_payload(user, token.key))


class LogoutView(APIView):
    @extend_schema(
        tags=["auth"],
        request=None,
        responses={200: {"type": "object", "properties": {"data": {"type": "object"}}}},
    )
    def post(self, request):
        if request.user.is_authenticated:
            Token.objects.filter(user=request.user).delete()
        logout(request)
        return envelope({"ok": True})


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["auth"], responses={200: UserMeSerializer})
    def get(self, request):
        return envelope(UserMeSerializer(request.user).data)
