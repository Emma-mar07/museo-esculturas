from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_public, name='lista_public'),
    # Si querés podés comentar la galería individual
    # path('galeria/', views.lista_obras, name='lista_obras'),
]