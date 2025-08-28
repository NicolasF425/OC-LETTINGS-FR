from django.urls import path
from lettings import views as lw


app_name = 'lettings'
urlpatterns = [
    path('', lw.index, name='index'),
    path('<int:letting_id>/', lw.letting, name='letting'),
]
