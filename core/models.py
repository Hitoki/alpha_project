from django.db import models
from django.contrib.auth.models import User, AbstractUser


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=18, null=True, blank=True)
#
#
# class AdminProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=18, null=True, blank=True)
#
#
# class SuperAdminProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=18, null=True, blank=True)
