from django.db import models


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


class Epoch(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField()


class Musician(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    instrument = models.ManyToManyField("Instrument")
