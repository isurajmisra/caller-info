from rest_framework import serializers
from ..models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('name', 'number', 'is_spam')

class CotactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'