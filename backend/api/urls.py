from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_url, name="create_url"),
    path("resolve/<str:short_url>", views.resolve_url, name="resolve_url"),
    path("stats/<str:analytics_id>", views.get_url_stats, name="get_url_stats"),
]
