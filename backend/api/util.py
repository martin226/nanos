import string
import random
import requests
from .models import URLShorten


def generate_id(k=6):
    short_url = "".join(random.choices(string.ascii_letters + string.digits, k=k))
    if URLShorten.objects.filter(short_url=short_url).exists():
        return generate_id()
    return short_url


def resolve_country_name(ip_address):
    r = requests.get(f"https://ipapi.co/{ip_address}/json/")
    if r.status_code != 200:
        return None
    data = r.json()
    return data.get("country_name")


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
