>>> from posts.models import Category
>>> from posts.serializers import CategorySerializer 
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> import io
>>> category = Category(name='Technologia',description='Kategoria o technologii')

>>> category.save()
>>> serializer=CategorySerializer(category)
>>> serializer.data
{'id': 6, 'name': 'Technologia', 'description': 'Kategoria o technologii'}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":6,"name":"Technologia","description":"Kategoria o technologii"}'
>>> stream = io.BytesIO(content)
>>> data=JSONParser().parse(stream)
>>> data
{'id': 6, 'name': 'Technologia', 'description': 'Kategoria o technologii'}
>>> deserializer=CategorySerializer(data=data)
>>> deserializer.is_valid()
True
>>> deserializer.fields 
{'id': IntegerField(read_only=True), 'name': CharField(max_length=60), 'description': CharField(allow_blank=True, allow_null=True, max_length=100, required=False)}
>>> deserializer.validated_data
{'name': 'Technologia', 'description': 'Kategoria o technologii'}
>>> new_category=deserializer.save()
>>> deserializer.data
{'id': 7, 'name': 'Technologia', 'description': 'Kategoria o technologii'}
>>> from posts.models import Topic
>>> from posts.serializers import TopicModelSerializer
>>> topic =Topic.objects.first()
>>> serializer=TopicModelSerializer(topic)
>>> serializer.data       
{'id': 2, 'name': 'Grzyby', 'category': 3, 'created': '2025-10-17T09:27:20.579329Z'}
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> import io
>>> content=JSONRenderer().render(serializer.data)   
>>> content
b'{"id":2,"name":"Grzyby","category":3,"created":"2025-10-17T09:27:20.579329Z"}'
>>> stream =io.BytesIO(content)
>>> data=JSONParser().parse(stream)
>>> data
{'id': 2, 'name': 'Grzyby', 'category': 3, 'created': '2025-10-17T09:27:20.579329Z'}
>>> deserializer=TopicModelSerializer(data=data)  
>>> deserializer.is_valid()
True
>>> deserializer.fields
{'id': IntegerField(label='ID', read_only=True), 'name': CharField(max_length=60), 'category': PrimaryKeyRelatedField(queryset=Category.objects.all()), 'created': DateTimeField(read_only=True)}
>>> deserializer.validated_data
{'name': 'Grzyby', 'category': <Category: Nieciekawe>}