from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_obras, name='lista_obras'),
]