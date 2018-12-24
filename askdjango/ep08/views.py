from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # perform_ 계열 함수를 통해, API 수행 결과를 DB에 반영하는 create/update/destroy 함수를 커스텀
    # serializer.save 함수에 키워드 인자를 함께 DB 에 적용
    def perform_create(self, serializer):
        serializer.save(ip=self.request.META['REMOTE_ADDR'])