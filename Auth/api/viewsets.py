from Auth import models
from rest_framework import viewsets
from Auth.api import serializers
from Auth import models

class AuthViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AuthSerializer
    queryset = models.Auth.objects.all()
