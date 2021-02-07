"""
The term application describes a Python package that
provides some set of features.
Applications may be reused in various projects.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    To configure an application, subclass AppConfig and
    put the dotted path to that subclass in INSTALLED_APPS.
    """
    name = 'users'
