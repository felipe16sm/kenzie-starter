from rest_framework.generics import ListAPIView
from kenzie_starter_app.models import Creator
from kenzie_starter_app.serializers import CreatorSerializer
from kenzie_starter_app.pagination import CustomPage


class CreatorListView(ListAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    pagination_class = CustomPage().setParams(10, 100)
