from django.urls import path

from . import views

app_name = 'spers'

urlpatterns = [
    path('', views.index, name='index'),
]
