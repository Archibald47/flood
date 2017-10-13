from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exp = models.IntegerField(default='0')

