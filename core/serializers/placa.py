from rest_framework.serializers import ModelSerializer
from core.models import Placa

class PlacaSerializer(ModelSerializer):
    class Meta:
        model = Placa
        fields = "__all__"