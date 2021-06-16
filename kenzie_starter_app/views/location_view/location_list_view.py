from kenzie_starter_app.models import Location
from kenzie_starter_app.serializers import LocationSerializer
from rest_framework.generics import ListAPIView


class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
