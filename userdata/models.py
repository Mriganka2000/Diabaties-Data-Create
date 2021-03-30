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
