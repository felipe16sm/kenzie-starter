from rest_framework import serializers

from kenzie_starter_app.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        depth = 2
