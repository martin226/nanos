from rest_framework.serializers import ModelSerializer
from .models import URLShorten


class URLShortenSerializer(ModelSerializer):
    class Meta:
        model = URLShorten
        fields = "__all__"
