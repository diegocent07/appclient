from django.urls import path

from . import views

urlpatterns = [
    path('', views.createOrder, name='index'),
    path('new/', views.FormDone, name='new')
    
]