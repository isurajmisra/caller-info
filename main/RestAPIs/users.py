from rest_framework.response import Response
from rest_framework.views import APIView

from ..Serializers import UserSerializer, UserDetailSerializer
from ..models import User, Contact
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class UserView(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        if request.user.is_superuser:
            users = self.queryset
            data = []
            for user in users:
                data.append(
                    {'id': user.id, 'name': user.name, 'number': user.number, 'email': user.email})
            return Response({'data': data})

        else:
            user = generics.get_object_or_404(User, id=request.user.id)
            data = {'id': user.id, 'name': user.name, 'number': user.number, 'email': user.email}
            return Response(data)
        return Response({'result': 'You are not authorized to see the result.'}, status=401)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['password'] == serializer.validated_data['confirm_password']:
                serializer.validated_data.pop('confirm_password', None)
                user = serializer.save()
                user.set_password(serializer.validated_data['password'])
                user.save()
                return Response(serializer.data, status=201)
            else:
                return Response({'result': 'Both password should match.'})

        return Response(serializer.errors, status=400)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication ]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        user = self.queryset.filter(id=id).last()
        if request.user.is_superuser or request.user == user:
            data = {'id': user.id, 'name': user.name, 'number': user.number, 'email': user.email}
            return Response(data)
        return Response({'result': 'You are not authorized to see the result.'}, status=401)

    def put(self, request, id=None):
        user = self.queryset.filter(id=id).last()
        if request.user.is_superuser or request.user == user:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response({'result': 'You are not authorized to see the result.'}, status=401)

    def delete(self, request, id=None):
        user = self.queryset.filter(id=id).last()
        if request.user.is_superuser or request.user == user:
            user.delete()
            return Response(status=204)
        return Response({'result': 'You are not authorized to see the result.'}, status=401)


