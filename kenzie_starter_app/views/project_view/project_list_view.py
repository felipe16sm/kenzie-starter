from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from kenzie_starter_app.models import Project
from kenzie_starter_app.serializers import ProjectSerializer
from kenzie_starter_app.filters import ProjectFilter


class ProjectListView(ListAPIView):
    queryset = Project.objects.all().prefetch_related(
        "location", "subcategory", "creator"
    )
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
