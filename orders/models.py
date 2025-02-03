from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_status = models.CharField(max_length=255)
    shipping_address = models.TextField()

    def __str__(self):
        return str(self.user.username)
