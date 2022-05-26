from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path("api/create", views.create_url, name="create_url"),
    path("api/stats/<str:analytics_id>", views.get_url_stats, name="get_url_stats"),
    path("", RedirectView.as_view(url="/app")),
    path("<path:short_url>", views.redirect_url, name="redirect_url"),
]
