from rest_framework import serializers
from .models import Buyer

class CreateBuyerSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        buyer = Buyer.objects.create(**validated_data)
        return buyer

    class Meta:
        model = Buyer
        fields = ('id', 'names', 'surnames', 'address', 'city', 'estado_geo')
        extra_kwargs = {
            'names': {'required': True},
            'surnames': {'required': True},
            'address': {'required': True},
            'city': {'required': True},
            'estado_geo': {'default': 0}
        }