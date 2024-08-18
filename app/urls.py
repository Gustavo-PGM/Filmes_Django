from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<int:filme_id>/', views.detalhes, name='detalhes'),
]
