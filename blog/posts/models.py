from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)
    description=models.TextField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['name']

class Topic(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['name']

class Post(models.Model):
    title=models.CharField(max_length=150)
    text=models.TextField()
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    slug=models.SlugField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title #do zmiany 
    
    class Meta:
        ordering=['-created_at']