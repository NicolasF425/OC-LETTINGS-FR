"""
lettings/urls.py
Urls for the lettings app
include custom errors 404 and 500 managing
"""

from django.urls import path
from lettings import views as lw


app_name = 'lettings'
urlpatterns = [
    path('', lw.index, name='index'),
    path('<int:letting_id>/', lw.letting, name='letting'),
]
handler404 = "oc_lettings_site.views.custom_404_view"
handler500 = "oc_lettings_site.views.custom_500_view"
