from rest_framework.viewsets import ModelViewSet
from ep04.models import Post
from ep04.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # class 내에 queryset에 조건을 추가할때 사용.
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(title__icontains='1')
        return qs