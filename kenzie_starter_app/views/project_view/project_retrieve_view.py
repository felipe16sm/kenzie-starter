from rest_framework.generics import RetrieveAPIView

from kenzie_starter_app.models import Project
from kenzie_starter_app.serializers import ProjectSerializer


class ProjectRetrieveView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
