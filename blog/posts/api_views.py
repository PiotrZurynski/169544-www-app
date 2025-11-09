from django.shortcuts import render
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Topic, Post
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import AllowAny
from .serializers import CategorySerializer,TopicModelSerializer,PostModelSerializer
User=get_user_model()
from rest_framework.views import APIView
from django.db import IntegrityError

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

class PostList(APIView):
    permission_classes=[AllowAny]
    authentication_classes=[]

    def get(self,request):
        qs=Post.objects.all()
        ser=PostModelSerializer(qs,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=PostModelSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        try:
            if request.user and request.user.is_authenticated:
                ser.save(created_by=request.user)
            else:
                try:
                    ser.save()
                except IntegrityError:
                    user=User.objects.first()
                    if not user:
                        return Response({"detail":"Brak użytkownika w bazie, a created_by nie jest nullable."},status=400)
                    ser.save(created_by=user)
        except Exception as e:
            return Response({"detail":str(e)},status=400)
        return Response(ser.data,status=status.HTTP_201_CREATED)

class PostDetail(APIView):
    permission_classes=[AllowAny]
    authentication_classes=[]

    def get(self,request,pk):
        obj=get_object_or_404(Post,pk=pk)
        ser=PostModelSerializer(obj)
        return Response(ser.data)

    def put(self,request,pk):
        obj=get_object_or_404(Post,pk=pk)
        ser=PostModelSerializer(obj,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=400)

    def delete(self,request,pk):
        obj=get_object_or_404(Post,pk=pk)
        obj.delete()
        return Response(status=204)

class PostSearch(APIView):
    permission_classes=[AllowAny]
    authentication_classes=[]

    def get(self,request):
        q=request.query_params.get('title','')
        qs=Post.objects.filter(title__icontains=q) if q else Post.objects.all()
        ser=PostModelSerializer(qs,many=True)
        return Response(ser.data)