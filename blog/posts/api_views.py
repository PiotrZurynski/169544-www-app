from django.shortcuts import render
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Topic, Post
from .permissions import CustomDjangoModelPermissions
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,AllowAny,IsAuthenticated
from .serializers import CategorySerializer,TopicModelSerializer,PostModelSerializer
User=get_user_model()

@api_view(['GET','POST'])
def category_list(request):
    if request.method=='GET':
        categories =Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category=Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def category_search(request):
    search_query=request.query_params.get('name', '')
    
    if search_query:
        categories=Category.objects.filter(name__icontains=search_query)
    else:
        categories=Category.objects.all()
    
    serializer=CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_topics(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    topics = Topic.objects.filter(category=category)
    serializer = TopicModelSerializer(topics, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def topic_list(request):
    if request.method=='GET':
        topics=Topic.objects.all()
        serializer=TopicModelSerializer(topics, many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=TopicModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def topic_detail(request, pk):
    try:
        topic=Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=TopicModelSerializer(topic)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=TopicModelSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def topic_search(request):
    search_query=request.query_params.get('name', '')
    
    if search_query:
        topics=Topic.objects.filter(name__icontains=search_query)
    else:
        topics=Topic.objects.all()
    
    serializer=TopicModelSerializer(topics, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method=='GET':
        posts=Post.objects.all()
        serializer=PostModelSerializer(posts,many=True)
        return Response(serializer.data)
    serializer=PostModelSerializer(data=request.data)
    if serializer.is_valid():
        if request.user.is_authenticated:
            user=request.user
        else:
            user=User.objects.first()
            if not user:
                return Response({"error":"Brak użytkownika w bazie"},status=status.HTTP_400_BAD_REQUEST)
        serializer.save(created_by=user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PostModelSerializer(post)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def post_update(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PostModelSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_delete(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def post_search(request):
    search_query=request.query_params.get('title', '')
    if search_query:
        posts=Post.objects.filter(title__icontains=search_query)
    else:
        posts=Post.objects.all()
    
    serializer=PostModelSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_posts(request):
    posts = Post.objects.filter(created_by=request.user)
    serializer = PostModelSerializer(posts, many=True)
    return Response(serializer.data)

class PostListAPIView(APIView):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    def get_queryset(self):
        return Post.objects.all()
    
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PostModelSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = User.objects.first()
                if not user:
                    return Response(
                        {"error": "Brak usera w bazie"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            serializer.save(created_by=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    
    def get_queryset(self):
        return Post.objects.all()
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostModelSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostModelSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)