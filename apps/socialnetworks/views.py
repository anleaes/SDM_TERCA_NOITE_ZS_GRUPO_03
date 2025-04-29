from .models import SocialNetwork
from rest_framework import viewsets
from .serializers import SocialNetworkSerializer

# Após o comentario "# Create your views here." e crie as views "SocialNetwork".

class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer  