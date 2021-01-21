from django.urls import path
from parks import views

urlpatterns = [
    path('', views.get_parks, name='get_parks'),
]