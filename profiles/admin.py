"""
profiles/admin.py
This file is used to register the applications in the admin console
"""

from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
