from django.urls import path
from . import views

urlpatterns = [
    path('entradas/', views.lista_entradas, name='lista_entradas'),
    path('autor/<int:autor_id>/', views.autor_entradas, name='autor_entradas')
]
