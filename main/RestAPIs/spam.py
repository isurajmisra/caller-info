from rest_framework.response import Response
from ..Serializers import SpamSerializer
from ..models import SpamContact, User, Contact
from rest_framework import generics, exceptions
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


class SpamView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    queryset = SpamContact.objects.all()
    serializer_class = SpamSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, user_id=None):
        user = User.objects.filter(id=user_id).first()
        if request.user == user:
            queryset = self.queryset.filter(user=user)
        else:
            raise exceptions.PermissionDenied
        result = []
        for spam in queryset:
            result.append({
                'name': spam.name,
                'number': spam.number
            })
        return Response(result)

    def post(self, request, user_id=None):
        user = User.objects.filter(id=user_id).first()
        if request.user == user:
            serializer = SpamSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            registered_user = User.objects.filter(id=user_id,number=serializer.validated_data['number']).first()
            contacts = Contact.objects.filter(user=user ,number=serializer.validated_data['number'])
            if registered_user:
                registered_user.is_spam = True
                registered_user.save()
            elif contacts:
                for contact in contacts:
                    contact.is_spam = True
                    contact.save()
            spam = serializer.save()
            spam.user = user
            spam.save()
        else:
            raise exceptions.PermissionDenied
        return Response(serializer.data, status=201)



