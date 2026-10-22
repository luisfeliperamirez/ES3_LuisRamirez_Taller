from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('album/<int:id>/', views.detalle_album, name='detalle_album'),
]