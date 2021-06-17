from django.db import models
from .location_model import Location
from .subcategory_model import Subcategory
from .creator_model import Creator


class Project(models.Model):
    class StateChoices(models.TextChoices):
        failed = "failed"
        live = "live"
        canceled = "canceled"
        successful = "successful"

    name = models.CharField(max_length=255)
    description = models.TextField()
    backers = models.IntegerField()
    created_at = models.DateTimeField()
    deadline = models.DateField()
    goal = models.FloatField()
    pledged = models.FloatField()
    usd_pledged = models.FloatField()
    currency = models.CharField(max_length=255)
    launched_at = models.DateTimeField()
    state = models.TextField(choices=StateChoices.choices)
    state_changed_at = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    creator = models.ForeignKey(Creator, on_delete=models.PROTECT)

    class Meta:
        ordering = ["name", "state"]
        indexes = [models.Index(fields=["name", "state"])]
