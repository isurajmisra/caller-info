from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import login as user_login, logout as user_logout
from rest_framework.views import APIView
from .Serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        user_logout(request)
        # request.user.auth_token.delete()
        return Response(status=204)


