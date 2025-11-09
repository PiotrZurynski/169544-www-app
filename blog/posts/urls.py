from django.urls import path
from . import api_views as views
from .api_views import PostList,PostDetail,PostSearch

urlpatterns = [
    path('categories/', views.category_list, name='category-list'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
    path('categories/search/', views.category_search, name='category-search'),
    path('topics/', views.topic_list, name='topic-list'),
    path('topics/<int:pk>/', views.topic_detail, name='topic-detail'),
    path('topics/search/', views.topic_search, name='topic-search'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/search/',PostSearch.as_view(),name='post-search'),
]