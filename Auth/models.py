from django.db import models

# Create your models here.

class Auth(models.Model):
    rdifCode = models.CharField(primary_key=True, editable=False, max_length=16)
    name = models.CharField(max_length=255)
    created_DateTime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
