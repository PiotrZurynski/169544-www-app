import graphene
from graphene_django import DjangoObjectType
from posts.models import Category, Topic, Post
from django.contrib.auth.models import User
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "description")

class TopicType(DjangoObjectType):
    class Meta:
        model = Topic
        fields = ("id", "name", "category", "created")
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")

class PostType(DjangoObjectType):
    created_by = graphene.Field(UserType)
    class Meta:
        model = Post
        fields = ("id", "title", "text", "slug", "topic", "created_at", "updated_at", "created_by")

class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id=graphene.Int(required=True))
    all_topics = graphene.List(TopicType)
    topic_by_id = graphene.Field(TopicType, id=graphene.Int(required=True))
    all_posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.Int(required=True))
    categories_by_name = graphene.List(CategoryType, name_fragment=graphene.String(required=True))
    posts_by_slug = graphene.List(PostType, slug_fragment=graphene.String(required=True))
    posts_count_by_user = graphene.Int(user_id=graphene.Int(required=True))

    def resolve_all_categories(root, info):
        return Category.objects.all()
    
    def resolve_category_by_id(root, info, id):
        try:
            return Category.objects.get(pk=id)
        except Category.DoesNotExist:
            raise Exception(f'Category with id {id} not found')
    
    def resolve_all_topics(root, info):
        return Topic.objects.select_related("category").all()
    
    def resolve_topic_by_id(root, info, id):
        try:
            return Topic.objects.get(pk=id)
        except Topic.DoesNotExist:
            raise Exception(f'Topic with id {id} not found')
    
    def resolve_all_posts(root, info):
        return Post.objects.select_related("topic", "created_by").all()
    
    def resolve_post_by_id(root, info, id):
        try:
            return Post.objects.get(pk=id)
        except Post.DoesNotExist:
            raise Exception(f'Post with id {id} not found')
    
    def resolve_categories_by_name(root, info, name_fragment):
        return Category.objects.filter(name__icontains=name_fragment)
    
    def resolve_posts_by_slug(root, info, slug_fragment):
        return Post.objects.select_related("topic", "created_by").filter(slug__icontains=slug_fragment)
    
    def resolve_posts_count_by_user(root, info, user_id):
        return Post.objects.filter(created_by_id=user_id).count()
    
class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)
    success = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String(required=True)
        slug = graphene.String(required=True)
        topic_id = graphene.Int(required=True)
        created_by_id = graphene.Int(required=True)

    def mutate(self, info, title, text, slug, topic_id, created_by_id):
        try:
            post = Post.objects.create(
                title=title,
                text=text,
                topic_id=topic_id,
                slug=slug,
                created_by_id=created_by_id
            )
            return CreatePost(post=post, success=True, message="Post created successfully")
        except Exception as e:
            return CreatePost(post=None, success=False, message=str(e))

class UpdatePost(graphene.Mutation):
    post = graphene.Field(PostType)
    success = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        text = graphene.String()
        topic_id = graphene.Int()
        slug = graphene.String()

    def mutate(self, info, id, title=None, text=None, topic_id=None, slug=None):
        try:
            post = Post.objects.get(id=id)
            if title:
                post.title = title
            if text:
                post.text = text
            if topic_id:
                post.topic_id = topic_id
            if slug:
                post.slug = slug
            post.save()
            return UpdatePost(post=post, success=True, message="Post updated successfully")
        except Post.DoesNotExist:
            return UpdatePost(post=None, success=False, message="Post not found")
        except Exception as e:
            return UpdatePost(post=None, success=False, message=str(e))

class DeletePost(graphene.Mutation):
    success = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return DeletePost(success=True, message="Post deleted successfully")
        except Post.DoesNotExist:
            return DeletePost(success=False, message="Post not found")
        except Exception as e:
            return DeletePost(success=False, message=str(e))

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)