from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #Asignamos que a la dirección / mostrará la vista que está en views.post_list
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
    #Asignamos que a la dirección /post/<int> mostrará la vista que está en views.post_detail, 
    #además de dar automáticamente el número que este post ocupa en la BBDD para la dirección del navegador
]