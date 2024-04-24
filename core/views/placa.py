from rest_framework.viewsets import ModelViewSet
from core.models import Placa
from core.serializers import PlacaSerializer

class PlacaViewSet(ModelViewSet):
    queryset = Placa.objects.all()
    serializer_class = PlacaSerializer