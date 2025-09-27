"""
profiles/models.py
Models file for the profile app
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model class for profiles
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
