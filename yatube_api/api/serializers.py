from rest_framework import serializers

from posts.models import Post, Comment, Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'created', 'author', 'text', 'post']
        read_only_fields = ['post']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'title', 'slug', 'description']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

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
