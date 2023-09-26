from django.urls import path
from .import views
urlpatterns =[
        path('entradas/', views.lista_entradas, name='lista_entradas'),
        path('autor/<str:autor>/', views.filtro_entradas, name='filtro_entradas')
]
