from django.db import models


class Ad(models.Model):
    text = models.TextField()
    publication_data = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.SET_DEFAULT, default='Deleted')
    ad = models.Manager()


class User(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    rating = models.IntegerField(default=0)
    vip_status = models.BooleanField()
    photo = models.ImageField(null=True)
    user = models.Manager()
