from django.urls import path
from profiles import views as pw


app_name = 'profiles'
urlpatterns = [
    path('', pw.index, name='index'),
    path('<str:username>/', pw.profile, name='profile'),
]
