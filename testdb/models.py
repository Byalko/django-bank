from django.db import models

# Create your models here.
class Card(models.Model):
    id = models.PositiveIntegerField(null=False, blank=False, primary_key=True)
    summary = models.FloatField(null=True, blank=True, default=0.0)
