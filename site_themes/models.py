from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.template.loader import template_source_loaders
from django.template.loaders import cached
from django.utils.translation import ugettext_lazy as _
import os


__all__ = ['Theme', 'SiteTheme']


class Theme(models.Model):
    title = models.CharField(_('title'), max_length=50, unique=True)
    slug = models.SlugField(_('Theme name'), unique=True)
    description = models.TextField(_('description'), blank=True, null=True)
    #path = PathField(_('path'), unique=True, blank=True, \
    #        path=settings.SITE_THEMES_ROOT)

    objects = models.Manager()

    class Meta:
        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')

    def __unicode__(self):
        return self.title

    @property
    def path(self):
        return os.path.join(settings.SITE_THEMES_ROOT, self.slug)

    def get_template_path(self):
        return "%s/templates" % self.path

    def get_media_path(self):
        return "%s/media" % self.path


class SiteTheme(models.Model):
    site = models.OneToOneField(Site, verbose_name=_('site'), \
                                related_name='skin')
    theme = models.ForeignKey(Theme, verbose_name=_('theme'), \
                             related_name='sites')

    objects = models.Manager()

    class Meta:
        verbose_name = _('Site theme')
        verbose_name_plural = _('Site themes')

    def __unicode__(self):
        return u"%s: %s" % (self.site, self.theme)

    def save(self, *args, **kwargs):
        super(SiteTheme, self).save(*args, **kwargs)
        Site.objects.clear_cache()

    @property
    def slug(self):
        return self.theme.slug
