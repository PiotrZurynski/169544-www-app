from django.urls import path
from . import api_views as viewss
from . import views 


urlpatterns = [
    path('categories/', viewss.category_list, name='category-list'),
    path('categories/<int:pk>/', viewss.category_detail, name='category-detail'),
    path('categories/search/', viewss.category_search, name='category-search'),
    path('categories/<int:pk>/topics/', viewss.category_topics, name='category-topics'),
    path('topics/', viewss.topic_list, name='topic-list'),
    path('topics/<int:pk>/', viewss.topic_detail, name='topic-detail'),
    path('topics/search/', viewss.topic_search, name='topic-search'),
    path('posts/', viewss.post_list, name='post-list'),
    path('posts/<int:pk>/', viewss.post_detail, name='post-detail'),
    path('posts/<int:pk>/update/', viewss.post_update, name='post-update'),
    path('posts/<int:pk>/delete/', viewss.post_delete, name='post-delete'),
    path('posts/search/',viewss.post_search,name='post-search'),
    path('users/posts/', viewss.user_posts, name='user-posts'),
    path('post-view/<int:pk>/', views.post_view, name='post-view'),
    path('edit-post/<int:pk>/', views.edit_post_view, name='edit-post'),
     path('posts-cbv/', viewss.PostListAPIView.as_view(), name='post-list-cbv'),
    path('posts-cbv/<int:pk>/', viewss.PostDetailAPIView.as_view(), name='post-detail-cbv'),
]