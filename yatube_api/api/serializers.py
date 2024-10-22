from rest_framework import serializers
from posts.models import Post, Comment, Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'created', 'author', 'text', 'post']

    def get_author(self, obj):
        return str(obj.author)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'title', 'slug', 'description']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    comments = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'text',
            'pub_date',
            'author',
            'image',
            'group',
            'comments'
        ]

    def get_author(self, obj):
        return str(obj.author)
