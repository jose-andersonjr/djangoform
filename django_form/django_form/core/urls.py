from django.urls import path
from django_form.core import views


urlpatterns = [
    path('', views.home, name='home'),
]