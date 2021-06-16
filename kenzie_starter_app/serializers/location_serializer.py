from django.db.models import fields
from kenzie_starter_app.models import Location

from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
