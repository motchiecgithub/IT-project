from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('translate/', views.translate, name='translate'),
    path('home/', views.home, name='home'),
    path('translate_c/', views.translate_C, name='translate_c'),
]