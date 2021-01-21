from django.urls import path
from playgrounds import views

urlpatterns = [
    path('', views.get_playgrounds, name='get_playgrounds'),
]