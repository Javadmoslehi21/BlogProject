from django.urls import path
from . import views

urlpatterns = [
    path('detail/<slug:slug>', views.post_detail, name='post_detail'),
    path('post_list', views.post_list, name='post_list'),
    path('search/', views.search, name='search_posts'),
    path('contactus/', views.contactus, name='contactus'),
]
