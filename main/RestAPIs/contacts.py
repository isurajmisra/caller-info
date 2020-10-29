from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import exceptions
from ..models import Contact, User
from ..Serializers import ContactSerializer, CotactDetailSerializer
from rest_framework import generics
from rest_framework import permissions


class ContactListView(generics.GenericAPIView):
    authentication_classes = [ SessionAuthentication, TokenAuthentication]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, user_id=None):
        if request.user.is_superuser:
            contacts = self.queryset
            data = []
            for contact in contacts:
                data.append(
                    {'id': contact.id, 'name': contact.name, 'number': contact.number, 'is_spam':contact.is_spam})
            return Response({'data': data})

        else:
            user = generics.get_object_or_404(User, id=user_id)
            contacts = self.queryset.filter(user=user)
            data = []
            for contact in contacts:
                data.append(
                    {'id': contact.id, 'name': contact.name, 'number': contact.number, 'is_spam':contact.is_spam})
            return Response(data)
        return Response({'result': 'You are not authorized to see the result.'}, status=401)

    def post(self, request, user_id=None):
        user = generics.get_object_or_404(User, id=user_id)
        if request.user == user:
            serializer = ContactSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            contact = serializer.save()
            contact.user = user
            contact.save()
            return Response(serializer.data, status=201)
        else:
            raise exceptions.PermissionDenied



class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [ SessionAuthentication, TokenAuthentication]
    queryset = Contact.objects.all()
    serializer_class = CotactDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, user_id=None, contact_id=None):
        user = User.objects.filter(id=user_id).last()
        contact = self.queryset.filter(id=contact_id).last()
        if (request.user.is_superuser or request.user == user) and contact:
            data = {'id': contact.id, 'name': contact.name, 'number': contact.number}
            return Response(data)
        return Response({'result': 'You are not authorized to see the result.'}, status=401)

    def put(self, request, user_id=None, contact_id=None):
        user = User.objects.filter(id=user_id).last()
        contact = self.queryset.filter(id=contact_id).last()
        if request.user.is_superuser or request.user == user:
            serializer = ContactSerializer(contact, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response({'result': 'You are not authorized to see the result.'}, status=401)

    def delete(self, request, user_id=None, contact_id=None):
        user = User.objects.filter(id=user_id).last()
        contact = self.queryset.filter(id=contact_id).last()
        if request.user.is_superuser or request.user == user:
            contact.delete()
            return Response(status=204)
        return Response({'result': 'You are not authorized to see the result.'}, status=401)