"""
profiles/urls.py
Urls for the profiles app
include custom errors 404 and 500 managing
"""

from django.urls import path
from profiles import views as pw


app_name = 'profiles'
urlpatterns = [
    path('', pw.index, name='index'),
    path('<str:username>/', pw.profile, name='profile'),
]
handler404 = "oc_lettings_site.views.custom_404_view"
handler500 = "oc_lettings_site.views.custom_500_view"
