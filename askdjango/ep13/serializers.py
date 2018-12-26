from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Post


class PostSerializer(ModelSerializer):
    author_name = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author_name', 'message', 'photo']