from rest_framework import serializers

from kenzie_starter_app.models import Creator


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = "__all__"
