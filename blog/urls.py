from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_public, name='lista_public'),
    
    # path('galeria/', views.lista_obras, name='lista_obras'),
]