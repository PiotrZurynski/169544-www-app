from django.contrib import admin

# Register your models here.
# modele musimy zaimportować
from .models import Category, Topic, Post
from django.utils.text import Truncator

# a następnie zarejestrować (pokazano najprostszy przypadek)




class PostAdmin(admin.ModelAdmin):
    readonly_fields=["created_at"]
    list_display=['title','short_text','topic','topic_with_category','slug','created_at','updated_at','created_by']
    def short_text(self,obj):
        return Truncator(obj.text).words(5,truncate="...")
    list_select_related=('topic','topic__category')
    def topic_with_category(self,obj):
        t=obj.topic
        if not t:
            return "-"
        cat=getattr(t,'category',None)
        if cat:
            return f"{t.name} ({cat.name})"
        return t.name
    list_filter=['topic','topic__category','created_by']
    prepopulated_fields={'slug':('title',)}
    
admin.site.register(Post,PostAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["name","description"]
    list_filter=['name']
admin.site.register(Category,CategoryAdmin)
class TopicAdmin(admin.ModelAdmin):
    list_display=["name","category","created"]
    list_filter=['name']
admin.site.register(Topic,TopicAdmin)