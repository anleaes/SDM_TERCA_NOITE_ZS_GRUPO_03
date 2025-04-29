from .models import  ClientSocialNetwork
from rest_framework import viewsets
from .serializers import ClientSocialnetworkSerializer

# Após o comentario "# Create your views here." e crie as views "Client".

class ClientSocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = ClientSocialNetwork.objects.all()
    serializer_class = ClientSocialnetworkSerializer
