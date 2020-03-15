from datetime import datetime

from django.db import models


class InstrumentManager(models.Manager):
    def get_queryset(self):
        return self


class Instrument(models.Model):
    SOPRANO = "SOP"
    ALTO = "ALT"
    TENOR = "TEN"
    BARITONE = "BAR"
    BASS = "BAS"
    RANGE_CHOICES = (
        (SOPRANO, "Soprano"),
        (ALTO, "Alto"),
        (TENOR, "Tenor"),
        (BARITONE, "Baritone"),
        (BASS, "Bass")
    )

    name = models.CharField(max_length=128)
    color = models.CharField(max_length=64, default="", blank=True)
    range = models.CharField(max_length=3, choices=RANGE_CHOICES, default=TENOR)
    epoch = models.ForeignKey("Epoch", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def get_color_name(self):
        return f"{self.color} {self.name}"


class Epoch(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Musician(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    instrument = models.ManyToManyField("Instrument")
    practising_hours = models.BigIntegerField(default=0)
    alive = models.BooleanField(default=True)
    bio = models.TextField()

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname
