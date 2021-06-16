from django.db.models import fields
from kenzie_starter_app.models import Category

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        depth = 2
