"""
lettings/admin.py
This file is used to register the applications in the admin console
"""

from django.contrib import admin

from .models import Letting
from .models import Address


admin.site.register(Letting)
admin.site.register(Address)
