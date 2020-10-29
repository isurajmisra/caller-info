from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import User, Contact, SpamContact

class SearchUserView(APIView):

    def get(self, request):
        name = request.GET.get('name', None)
        number = request.GET.get('number', None)
        queryset = []
        if name:
            user = User.objects.filter(name__icontains=name).first()
            contact_queryset = Contact.objects.filter(name__icontains=name).values_list('name', 'number',
                                                                                        'is_spam')
            exc_contact_queryset = Contact.objects.filter(name__icontains=name).values_list('name', 'number',
                                                                                        'is_spam').exclude(name=name)
            spam_queryset = SpamContact.objects.filter(name__icontains=name).values_list('name', 'number',
                                                                                         'is_spam').exclude(name=name)

            merged_queryset = contact_queryset.union(exc_contact_queryset, spam_queryset)
            if user:
                if Contact.objects.filter(user=request.user, number=user.number).first():
                    queryset.append({
                        "name":user.name,
                        "number":user.number,
                        "email":user.email,
                        "is_spam":user.is_spam
                    })
            for set in merged_queryset:
                queryset.append({
                    "name": set[0],
                    "number": set[1],
                    "is_spam": set[2]
                })



        elif number:
            exact_user = User.objects.filter(number=number).first()
            if exact_user :
                if Contact.objects.filter(user=request.user,number=exact_user.number).first():

                    return Response({
                            'name': exact_user.name,
                            'number': exact_user.number,
                            'email': exact_user.email,
                            'spam': exact_user.is_spam
                        })
            elif exact_user:
                return Response({
                    'name': exact_user.name,
                    'number': exact_user.number,
                    'spam': exact_user.is_spam
                })
            else:

                contact_queryset = Contact.objects.filter(number__icontains=number).values_list('name', 'number',
                                                                                            'is_spam')
                spam_queryset = SpamContact.objects.filter(number__icontains=number).values_list('name', 'number',
                                                                                             'is_spam')
                merged_queryset = contact_queryset.union(spam_queryset)
                for set in merged_queryset:
                    queryset.append({
                        "name": set[0],
                        "number": set[1],
                        "is_spam": set[2]
                    })

        return Response(queryset)


