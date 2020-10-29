from rest_framework import serializers, exceptions, generics

from django.contrib.auth import authenticate
from ..models import User, Contact
from rest_framework.response import Response

class LoginSerializer(serializers.Serializer):
    number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        number = data['number'] or ""
        password = data['password'] or ""
        if number and password:
            user = User.objects.filter(number=number).first()
            if user:
                if user.check_password(password):
                    data['user'] = user
                else:
                    msg = "Unable to login with given credentials."
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Number is not registered."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Please provide number and password both."
            raise exceptions.ValidationError(msg)
        return data
