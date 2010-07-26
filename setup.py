from setuptools import setup, find_packages

version = __import__('site_themes').get_version()

setup(
    name = "django-site-themes",
    version = version,
    description = "Ability change django project site theme (templates and static media) on fly without restart server",
    keywords="django skin theme dynamic media templates",
    author = "Alex Kamedov",
    author_email = "alex.k@3128.ru",
    url = "git@3128.ru:repos/django-skinability.git",
    license = "New BSD License",
    platforms = ["any"],
    classifiers = ["Development Status :: %s" % version,
                   "Environment :: Web Environment",
                   "Framework :: Django",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Utilities"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

