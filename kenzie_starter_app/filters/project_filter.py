from django_filters import rest_framework as filters

from kenzie_starter_app.models import Project


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Project
        fields = ["name"]
