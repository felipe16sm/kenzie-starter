from kenzie_starter_app.models import Subcategory
from kenzie_starter_app.serializers import SubcategorySerializer
from rest_framework.generics import ListAPIView


class SubcategoryListView(ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
