from django.urls import path
from . import api_views as views

urlpatterns = [
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
    path('categories/search/', views.category_search, name='category-search'),
    path('categories/<int:pk>/topics/', views.category_topics, name='category-topics'),
    path('topics/', views.topic_list, name='topic-list'),
    path('topics/<int:pk>/', views.topic_detail, name='topic-detail'),
    path('topics/search/', views.topic_search, name='topic-search'),
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/<int:pk>/update/', views.post_update, name='post-update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post-delete'),
    path('posts/search/',views.post_search,name='post-search'),
    path('users/posts/', views.user_posts, name='user-posts'),

]