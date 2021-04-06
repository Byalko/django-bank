from rest_framework import viewsets
from . import models
from . import serializers

class CardViewset(viewsets.ModelViewSet):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer