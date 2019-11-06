#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Management command entry point for working with migrations
"""

import sys, os
import django
from django.conf import settings

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # "django.contrib.admin",
    # "django.contrib.auth",
    # "django.contrib.contenttypes",
    "django.contrib.sites",
    # The ordering here, the apps using the organization base models
    # first and *then* the organizations app itself is an implicit test
    # that the organizations app need not be installed in order to use
    # its base models.
    "test_accounts",
    "test_abstract",
    "test_vendors",
    "organizations",
    "test_custom",
    "tests",
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "test2.sqlite3",
        }
    },
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES,  # Silence Django 1.7 warnings
    SITE_ID=1,
    FIXTURE_DIRS=['tests/fixtures'],
    # ORGS_SLUGFIELD='django_extensions.db.fields.AutoSlugField',
    ORGS_SLUGFIELD='autoslugged.AutoSlugField',
    # INVITATION_BACKEND='tests.backends.MyInvitationBackend',
    INSTALLED_APPS=INSTALLED_APPS,
    ROOT_URLCONF="tests.urls",
    STATIC_ROOT=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static'),
    STATIC_URL = '/static/',
)

django.setup()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
