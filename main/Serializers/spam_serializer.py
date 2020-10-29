from rest_framework import serializers
from ..models import SpamContact

class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamContact
        fields = ('name', 'number')


# class SpamCotactDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SpamContact
#         fields = '__all__'