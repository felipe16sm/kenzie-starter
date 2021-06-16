from django.urls import re_path

from .views import (
    ProjectListView,
    ProjectRetrieveView,
    CategoryListView,
    CategoryRetrieveView,
    CreatorListView,
    CreatorRetrieveView,
    LocationListView,
    LocationRetrieveView,
    SubcategoryListView,
    SubcategoryRetrieveView,
)

urlpatterns = [
    re_path(r"^projects/?$", ProjectListView.as_view()),
    re_path(r"^projects/(?P<pk>\w+)/?$", ProjectRetrieveView.as_view()),
    re_path(r"^categories/?$", CategoryListView.as_view()),
    re_path(r"^categories/(?P<pk>\w+)/?$", CategoryRetrieveView.as_view()),
    re_path(r"^creators/?$", CreatorListView.as_view()),
    re_path(r"^creators/(?P<pk>\w+)/?$", CreatorRetrieveView.as_view()),
    re_path(r"^locations/?$", LocationListView.as_view()),
    re_path(r"^locations/(?P<pk>\w+)/?$", LocationRetrieveView.as_view()),
    re_path(r"^subcategories/?$", SubcategoryListView.as_view()),
    re_path(r"^subcategories/(?P<pk>\w+)/?$", SubcategoryRetrieveView.as_view()),
]
