.. django-site-themes documentation master file, created by
   sphinx-quickstart on Thu Jul 22 16:12:20 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Документация к django-site-themes
=================================

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Описание
--------

``django-site-themes`` - это Django приложение, добавляющее возможность
смены темы оформления сайта без перезапуска сервера/демона проекта.
Тема оформления - это файлы шаблонов, используемых приложениями проекта, и 
используемая в шаблонах статика (CSS, JavaScript, images). Один ваш проект
может обслуживать несколько сайтов с похожим функционалом и разными темами
оформления.

``django-site-themes`` provides template loader, context processor and some 
models for store data about used and available themes. You can manage site 
themes in django admin.

Установка
---------

Данное приложение можно установить с помощью ``pip``::

    pip install -e git@github.com:alekam/django-site-themes.git

Измените файл настроек проекта примерно так как показано ниже::

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

Создайте папку для хранения тем. SITE_THEMES_ROOT должен указывать на нее.
Положите в нее темы для вашего проекта (о создании тем ниже).

Создайте необходимые таблицы, с помощью команды ``syncdb``::

    manage.py syncdb

Выполните ``install_theme`` для установки тем::

    manage.py install_theme

Презапустите проект, перейдите в административный раздел, найдите управление
моделями приложения ``Site Themes``, сопоставте нужный шаблон с нужным сайтом.

Принцип работы
--------------

Вся необходимая информация хранится в моделях приложения.

Для загрузки шаблонов используется 
``site_themes.template_loader.SiteThemeLoader``, который смотрит какую тему 
для какого сайта необходимо использовать и пытается загрузить требуемый 
шаблон от туда. Если это не удается, то используется следующий загрузчик 
шаблонов. 

В шаблонах темы, для указания пути к статике в качестве префикса используется 
``THEME_MEDIA_URL``. Эта переменная добавляется в контекст с помощью  
``site_themes.context_processor.site_theme_media``.

Команды
-------

install_theme
~~~~~~~~~~~~~

Сканирует содержимое ``SITE_THEMES_ROOT`` и добавляет найденный папки как
темы оформления, если они еще не зарегистрированы.


Структура темы оформления
-------------------------

Тема должна содержать две папки:

* ``media`` - содержит всю статику, используемую в шаблонах темы. 
При использовании поставляемого с этим приложением обработчика контекста
``site_theme_media``, в шаблонах доступна переменная ``THEME_MEDIA_URL``, 
которая указывает на папку `media`` используемой сайтом темы.

* ``templates`` - содержит предоставляемые темой шаблоны.
 
