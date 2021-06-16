from kenzie_starter_app.models import Category
from kenzie_starter_app.serializers import CategorySerializer
from rest_framework.generics import RetrieveAPIView


class CategoryRetrieveView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
