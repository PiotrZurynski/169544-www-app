from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required,login_required
from django.core.exceptions import PermissionDenied
from .models import Post

def post_view(request, pk):
    if not request.user.has_perm('posts.view_post'):
        raise PermissionDenied()   
    try:
        post = Post.objects.get(pk=pk)
        return HttpResponse(f"<h1>Post: {post.title}</h1><p>{post.text}</p><p>Autor: {post.created_by.username}</p>")
    except Post.DoesNotExist:
        return HttpResponse(f"W bazie nie ma posta o id={pk}.")
    
@login_required
def edit_post_view(request, pk):
    try:
        post=Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise PermissionDenied("Post nie istnieje")
    is_author = post.created_by == request.user
    can_edit_others = request.user.has_perm('posts.can_edit_others_posts')
    if not is_author and not can_edit_others:
        raise PermissionDenied("Brak uprawnien")
    permission_info = ""
    if is_author:
        permission_info = "jestes autorem"
    if can_edit_others:
        permission_info += "masz moderator forum"
    
    return HttpResponse(
        f"<h1>Edycja posta: {post.title}</h1>"
        f"<p><strong>Autor:</strong> {post.created_by.username}</p>"
        f"<p><strong>Zalogowany jako:</strong> {request.user.username}</p>"
        f"<p>{permission_info}</p>"
        f"<p><strong>Treść:</strong> {post.text}</p>"
    )