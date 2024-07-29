from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.user_login, name='user_login'),
    path('logout/',views.user_logout, name='user_logout'),
    path('register/',views.user_register, name='user_register'),
    path('user_edit/',views.user_edit, name='user_edit'),
]
