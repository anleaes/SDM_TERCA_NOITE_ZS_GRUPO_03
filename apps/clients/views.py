from .models import Client, ClientSocialNetwork
from rest_framework import viewsets
from .serializers import ClientSerializer, ClientSocialnetworkSerializer

# Após o comentario "# Create your views here." e crie as views "Client".

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer  

class ClientSocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = ClientSocialNetwork.objects.all()
    serializer_class = ClientSocialnetworkSerializer
