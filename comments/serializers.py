from rest_framework import serializers

from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'date_published', 'author', 'post', 'content', 'image',
                    'likes', 'dislikes']

