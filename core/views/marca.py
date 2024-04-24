from rest_framework.viewsets import ModelViewSet
from core.serializers import MarcaSerializer
from core.models import Marca

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer