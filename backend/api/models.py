from django.db import models

# Create your models here.


class URLShorten(models.Model):
    url = models.URLField(max_length=255)
    short_url = models.CharField(max_length=8, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.url


class View(models.Model):
    short_url = models.ForeignKey(
        URLShorten, on_delete=models.CASCADE, related_name="views"
    )
    viewed_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=255, null=True)
    ip = models.GenericIPAddressField(null=True)
    referrer = models.CharField(max_length=255, null=True)
    device = models.CharField(max_length=255, null=True)
