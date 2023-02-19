from django.db import models
from authentication.models import User

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


def upload_to(instance, filename):
    return f'car_photo/{instance.user.username}/{filename}'


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')
    make = models.CharField(
        max_length=30, default='Volvo', blank=True, null=True)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    url = models.URLField(blank=True, null=True, default=None)
