from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from kenzie_starter_app.models import Creator
from kenzie_starter_app.serializers import CreatorSerializer


class CreatorListView(ListAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
