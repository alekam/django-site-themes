from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured
from models import *


def site_theme_media(request):
    site = Site.objects.get_current()
    try:
        theme_name = site.skin.slug
    except SiteTheme.DoesNotExist:
        try:
            theme_name = Theme.objects.get(slug=settings.DEFAULT_THEME)
        except Theme.DoesNotExist:
            raise ImproperlyConfigured('Default theme is not exist!')
    return {
                'THEME_MEDIA_URL': '%s%s/media/' % (
                                    settings.SITE_THEMES_URL, theme_name),
            }
