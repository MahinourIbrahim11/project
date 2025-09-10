from django.urls import path
from .views import home, about, form_view

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('form/', form_view, name='form'),
]
