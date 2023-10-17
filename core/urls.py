from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import facial_recognition
urlpatterns = [
     path('', facial_recognition, name='facial_recognition'),
]
