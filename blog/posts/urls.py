from django.urls import path
from . import api_views as views

urlpatterns = [
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
    path('categories/search/', views.category_search, name='category-search'),
    path('topics/', views.topic_list, name='topic-list'),
    path('topics/<int:pk>/', views.topic_detail, name='topic-detail'),
    path('topics/search/', views.topic_search, name='topic-search'),
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/search/',views.post_search,name='post-search'),
]