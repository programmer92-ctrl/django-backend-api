from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=255)

    def __str__(self):
        return self.item_name
