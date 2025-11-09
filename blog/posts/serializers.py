from rest_framework import serializers
from .models import Category, Topic, Post
from django.utils import timezone

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
    topic_name=serializers.CharField(source='topic.name',read_only=True)
    category_name=serializers.CharField(source='topic.category.name',read_only=True)
    created_by_username=serializers.CharField(source='created_by.username',read_only=True)

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
        read_only_fields=['id','updated_at','created_by','topic_name','category_name','created_by_username']

        def validate_title(self,value):
            if not value.replace(' ','').isalpha():
                raise serializers.ValidationError(
                    "Pole może zawierać tylko litery"
                )
            return value
        
        def validate_created_at(self,value):
            if value and value > timezone.now():
                raise serializers.ValidationError(
                    "Data dodania nie może być z przyszłości"
                )
            return value