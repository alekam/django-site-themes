from django.contrib import admin
from models import *


class ThemeAdmin(admin.ModelAdmin):
    pass


class SiteThemeAdmin(admin.ModelAdmin):
    list_display = ['site', 'theme']
    list_filter = ['theme']
    raw_id_fields = ['site', 'theme']


admin.site.register(Theme, ThemeAdmin)
admin.site.register(SiteTheme, SiteThemeAdmin)
