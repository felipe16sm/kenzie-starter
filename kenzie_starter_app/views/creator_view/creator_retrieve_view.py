from rest_framework.generics import RetrieveAPIView

from kenzie_starter_app.models import Creator

from kenzie_starter_app.serializers import CreatorSerializer


class CreatorRetrieveView(RetrieveAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
