'''
Created on 22.07.2010

@author: volf
'''
from django.conf import settings
from django.core.management.base import NoArgsCommand
from site_themes.models import Theme
import os


class Command(NoArgsCommand):
    help = 'Find and install site themes'
    required_model_validation = True
    can_import_settings = True

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.installed = 0
        self.founded = 0
        self.already_installed = 0

    def handle(self, **options):
        """Find all themes in SITE_THEMES_ROOT and install it"""
        for root, dirs, files in os.walk(settings.SITE_THEMES_ROOT):
            for name in dirs:
                for t_root, t_dirs, t_files in \
                                        os.walk(os.path.join(root, name)):
                    if 'media' in t_dirs and 'templates' in t_dirs:
                        print "Found theme '%s'" % name
                        self.founded += 1
                        self.install_theme(name)

        print "\n%s themes installed, but %s founded and %s alresdy installed" % \
                (self.installed, self.founded, self.already_installed)


    def install_theme(self, name):
        """Install theme"""
        try:
            Theme.objects.get(slug=name)
            self.already_installed += 1
            print 'already installed'
        except Theme.DoesNotExist:
            print 'Install theme "%s"' % name
            Theme.objects.create(slug=name, title=name)
            self.installed += 1

