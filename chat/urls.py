from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:group>/', views.group, name='group'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:group>/', views.getMessages, name='getMessages')
]