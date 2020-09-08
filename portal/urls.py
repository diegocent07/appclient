from django.urls import path
from appclient import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.createOrder, name='index'),
    path('new/', views.FormDone, name='new')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)