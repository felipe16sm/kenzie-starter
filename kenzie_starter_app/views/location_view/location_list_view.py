from kenzie_starter_app.models import Location
from kenzie_starter_app.serializers import LocationSerializer
from rest_framework.generics import ListAPIView
from kenzie_starter_app.pagination import CustomPage


class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = CustomPage().setParams(10, 100)
