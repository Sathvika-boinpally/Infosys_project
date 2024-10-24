from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    hospital_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Override related names to avoid conflicts with Django's default User model
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Custom related name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # Custom related name to avoid conflict
        blank=True
    )
