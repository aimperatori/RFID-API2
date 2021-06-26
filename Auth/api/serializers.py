from rest_framework import serializers
from Auth import models

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Auth
        fields = '__all__'