from .models import ClientSocialNetwork
from rest_framework import serializers


class ClientSocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSocialNetwork
        fields = '__all__'
