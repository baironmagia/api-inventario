from rest_framework import serializers
from api.models  import Proeducto

class ProductoSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Proeducto
        fields = '__all__'