from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #Asignamos que a la dirección / mostrará la vista que está en views.post_list
]