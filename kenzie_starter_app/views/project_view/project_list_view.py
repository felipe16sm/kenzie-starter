from rest_framework.generics import ListAPIView
from kenzie_starter_app.models import Project
from kenzie_starter_app.serializers import ProjectSerializer
from kenzie_starter_app.filters import ProjectFilter
from kenzie_starter_app.pagination import CustomPage


class ProjectListView(ListAPIView):
    queryset = Project.objects.all().prefetch_related(
        "location", "subcategory", "creator"
    )
    serializer_class = ProjectSerializer
    pagination_class = CustomPage().setParams(10, 100)
    filterset_class = ProjectFilter
