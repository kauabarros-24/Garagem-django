from rest_framework.viewsets import ModelViewSet
from core.serializers import CarroListSerialzier, CarroSerializer
from core.models import Carro

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CarroListSerialzier
        return CarroSerializer