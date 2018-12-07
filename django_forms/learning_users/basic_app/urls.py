from django.urls import path, include
from basic_app import views

#app name


urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('index/', views.index, name = 'index')
]
