from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articulo/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
    path('seguir/', views.seguir_blog, name='seguir_blog'),
    path('perfil/', views.perfil, name='perfil'),
]
