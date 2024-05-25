from django.urls import path
from recipes import views


urlpatterns = [
    path('', views.home),
    path('contato/', views.contato),
    path('sobre/', views.sobre),
]
