from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_user_agents.utils import get_user_agent
from .util import generate_id, resolve_country_name, get_client_ip
from .models import URLShorten

validate = URLValidator()

# Create your views here.


@api_view(["POST"])
def create_url(request):
    data = request.data
    url = data.get("url")
    if not url:
        return Response({"error": "URL is required"}, status=400)
    try:
        validate(url)
    except ValidationError:
        return Response({"error": "Invalid URL"}, status=400)
    short_url, analytics_id = generate_id(), generate_id()
    url_shorten = URLShorten(url=url, short_url=short_url, analytics_id=analytics_id)
    url_shorten.save()
    return Response({"short_url": short_url, "analytics_id": analytics_id}, status=201)


@api_view(["GET"])
def resolve_url(request, short_url):
    qs = URLShorten.objects.filter(short_url=short_url)
    if qs.count() != 1:
        return Response({"error": "Short URL not found"}, status=404)
    url_shorten = qs.first()

    if not url_shorten.is_active:
        return Response({"error": "Short URL not found"}, status=404)

    ip_address = get_client_ip(request)
    country_name = resolve_country_name(ip_address)
    if not country_name:
        country_name = "N/A"
    referrer = request.META.get("HTTP_REFERER")
    if not referrer:
        referrer = "N/A"
    user_agent = get_user_agent(request)
    if user_agent.is_pc:
        device = "PC"
    elif user_agent.is_mobile:
        device = "Mobile"
    elif user_agent.is_tablet:
        device = "Tablet"
    else:
        device = "Other"

    url_shorten.views.create(
        ip=ip_address, country=country_name, referrer=referrer, device=device
    )
    return Response({"url": url_shorten.url})


@api_view(["GET"])
def get_url_stats(request, analytics_id):
    qs = URLShorten.objects.filter(analytics_id=analytics_id)
    if qs.count() != 1:
        return Response({"error": "Analytics ID not found"}, status=404)
    url_shorten = qs.first()
    views = url_shorten.views.count()
    unique_views = url_shorten.views.values("ip").distinct().count()
    country_views = (
        url_shorten.views.values("country")
        .annotate(count=models.Count("country"))
        .order_by("-count")
    )
    referrer_views = (
        url_shorten.views.values("referrer")
        .annotate(count=models.Count("referrer"))
        .order_by("-count")
    )
    device_views = (
        url_shorten.views.values("device")
        .annotate(count=models.Count("device"))
        .order_by("-count")
    )
    return Response(
        {
            "url": url_shorten.url,
            "short_url": url_shorten.short_url,
            "views": views,
            "unique_views": unique_views,
            "country_views": country_views,
            "referrer_views": referrer_views,
            "device_views": device_views,
        }
    )
