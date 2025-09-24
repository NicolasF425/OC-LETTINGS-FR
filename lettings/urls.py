from django.urls import path
from lettings import views as lw


app_name = 'lettings'
urlpatterns = [
    path('', lw.index, name='index'),
    path('<int:letting_id>/', lw.letting, name='letting'),
]
handler404 = "oc_lettings_site.views.custom_404_view"
handler500 = "oc_lettings_site.views.custom_500_view"
