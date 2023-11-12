from django.urls import path
from . import views

app_name="phonetic"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('translate/', views.translate, name='translate'),
    path('main/', views.main, name='main'),
    path('translate_c/', views.translate_C, name='translate_c'),
    path('translate_c/process_word_link/', views.process_word_link, name = 'process_word_link'),

]
