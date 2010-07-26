.. django-site-themes documentation master file, created by
   sphinx-quickstart on Thu Jul 22 16:12:20 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-site-themes documentation!
==============================================

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Overview
--------

``django-site-themes`` is an application that adds ability to Django 
project to change site theme on fly without restart project instance.
Theme is a project template files and static media files (CSS, JavaScript, 
images). Your one project instance can serve many sites with similar 
functionality and different themes.

``django-site-themes`` provides template loader, context processor and some 
models for store data about used and available themes. You can manage site 
themes in django admin.

Install
-------

Install the application via ``pip``::

    pip install -e git@github.com:alekam/django-site-themes.git

Change your project settings like this::

    INSTALLED_APPS = (
        ...
        'site_themes',
    )

    TEMPLATE_LOADERS = (
        'site_themes.template_loader.SiteThemeLoader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
    )
    
    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'site_themes.context_processor.site_theme_media',
    )
    
    DEFAULT_THEME = 'my_default_theme'
    SITE_THEMES_ROOT = os.path.join(MEDIA_ROOT, 'themes')
    SITE_THEMES_URL = MEDIA_URL + 'themes/'

Copy ``django-site-themes`` media folder or create symlink to ``themes`` in your
media root. Put your themes in this folder. 

Run ``install_theme`` management command to install your themes::

    manage.py install_theme


Management commands
-------------------

install_theme
~~~~~~~~~~~~~

Scan ``SITE_THEMES_ROOT`` folder and try to add founded themes if it is not 
registered in database.


Theme structure
---------------

Theme must consist of two folders:

* ``media`` with theme static files (images, scripts and styles). 
if you use ``site_theme_media`` context processor, ``THEME_MEDIA_URL`` 
available in templates and points to `media`` folder.

* ``templates`` with theme templates, it is used for first of TEMPLATE_DIRS 
folder.
 

How it works
------------

site_themes.template_loader.SiteThemeLoader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try load template from theme. If theme does not provide required template,
it try to load from ``TEMPLATE_DIRS`` of project settings.

site_themes.context_processor.site_theme_media
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds ``THEME_MEDIA_URL`` to context, witch is used in theme templates to put 
path to used theme media.


Used constants and variables
----------------------------

defined in project settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

SITE_THEMES_ROOT - root path with all available themes
SITE_THEMES_URL - url to themes 
DEFAULT_THEME - slug of default theme

defined by site_themes.context_processor.site_theme_media
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
THEME_MEDIA_URL - URL to media files of used theme 


Known problems
--------------

* ``django.template.loaders.cached.Loader`` is not supported

