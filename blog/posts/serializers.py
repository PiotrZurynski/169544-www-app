from rest_framework import serializers
from .models import Category, Topic, Post

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)
    description = serializers.CharField(
        max_length=100, 
        required=False, 
        allow_blank=True, 
        allow_null=True
    )
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class TopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'category','created']
        read_only_fields = ['id', 'created']

class PostModelSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = [
            'id', 
            'title', 
            'text', 
            'slug',
            'topic', 
            'topic_name',
            'category_name',
            'created_by',
            'created_by_username',
            'created_at', 
            'updated_at'
        ]
        read_only_fields=['id','created_at','updated_at','created_by']

        