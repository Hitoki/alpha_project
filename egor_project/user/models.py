from django.db import models


class UserObject(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    rating = models.IntegerField(default=0)
    vip_status = models.BooleanField()
