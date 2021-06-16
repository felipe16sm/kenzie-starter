from django.db.models import fields
from kenzie_starter_app import models
from kenzie_starter_app.models import Subcategory
from rest_framework import serializers


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"
