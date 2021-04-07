from django.db import models


class UserData(models.Model):
    LEVEL_CHOICES = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High")
    )

    HEALING_CHOICES = (
        ("Slow", "Slow"),
        ("Fast", "Fast")
    )

    peeatnight = models.BooleanField()
    peelevel = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    thirstylevel = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    feeltired = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    blurryvision = models.BooleanField()
    healing = models.CharField(max_length=100, choices=HEALING_CHOICES)
    hungrylevel = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    skin = models.BooleanField()
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    age = models.IntegerField(default=0)
    noofpregnency = models.IntegerField(default=0, blank=True, null=True)


class OriginalData(models.Model):
    pregnency = models.IntegerField(default=0, blank=True, null=True)
    bmi = models.FloatField(default=0)

