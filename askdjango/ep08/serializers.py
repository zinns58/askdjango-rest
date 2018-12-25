from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Post


class PostSerializer(ModelSerializer):
    # 커스텀 필드 추가
    author_username = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['author_username', 'message']