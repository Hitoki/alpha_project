from django.db import models


class Instrument(models.Model):
    name = models.CharField(max_length=128, default="", )  # not required
    color = models.CharField(max_length=128)  # required
    strings = models.IntegerField(max_length=50, default=1, blank=True, null=True)
    epoch = models.ForeignKey("Epoch", on_delete=models.SET_NULL, blank=True, null=True)


class Epoch(models.Model):
    name = models.CharField(max_length=128, default="", )  # not required
    data = models.DateTimeField()

