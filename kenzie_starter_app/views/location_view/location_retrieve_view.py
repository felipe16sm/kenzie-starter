from kenzie_starter_app.models import Location
from kenzie_starter_app.serializers import LocationSerializer
from rest_framework.generics import RetrieveAPIView


class LocationRetrieveView(RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
