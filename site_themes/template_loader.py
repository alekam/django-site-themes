from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured
from django.template.loaders.filesystem import Loader
from models import *


class SiteThemeLoader(Loader):
    """Load template for site"""
    def get_template_sources(self, template_name, template_dirs=None):
        """Returns the absolute paths to "template_name"."""
        try:
            template_dirs = [Site.objects.get_current().skin.\
                                        theme.get_template_path()]
        except SiteTheme.DoesNotExist: # no themes is set for current site 
            try: # try to use default theme
                template_dirs = [Theme.objects.\
                        get(slug=settings.DEFAULT_THEME).get_template_path()]
            except Theme.DoesNotExist:
                raise ImproperlyConfigured(
                    'Default theme "%s" is not registered!' % \
                                    settings.DEFAULT_THEME)
            except KeyError:
                raise ImproperlyConfigured(
                    'DEFAULT_THEME is not set in your project settings!')
        return super(SiteThemeLoader, self).\
                    get_template_sources(template_name, template_dirs)
