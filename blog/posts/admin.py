from django.contrib import admin

# Register your models here.
# modele musimy zaimportować
from .models import Category, Topic, Post

# a następnie zarejestrować (pokazano najprostszy przypadek)




class PostAdmin(admin.ModelAdmin):
    readonly_fields=["created_at"]
    list_display=['title','text','topic','slug','created_at','updated_at','created_by']
admin.site.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["name","descriptions"]
admin.site.register(Category)
class TopicAdmin(admin.ModelAdmin):
    list_display=["name","category","created"]

admin.site.register(Topic)