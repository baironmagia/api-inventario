from rest_framework import viewsets
from api.models import Proeducto
from api.serializer import ProductoSerealizer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Proeducto.objects.all()
    serializer_class = ProductoSerealizer
