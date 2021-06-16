from kenzie_starter_app.models import Category
from kenzie_starter_app.serializers import CategorySerializer
from rest_framework.generics import ListAPIView
from kenzie_starter_app.pagination import CustomPage


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPage().setParams(10, 100)
