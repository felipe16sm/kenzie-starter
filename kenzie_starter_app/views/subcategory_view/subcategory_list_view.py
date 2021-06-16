from kenzie_starter_app.models import Subcategory
from kenzie_starter_app.serializers import SubcategorySerializer
from rest_framework.generics import ListAPIView
from kenzie_starter_app.pagination import CustomPage


class SubcategoryListView(ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    pagination_class = CustomPage().setParams(10, 100)
