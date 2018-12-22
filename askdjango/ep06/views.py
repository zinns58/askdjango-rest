from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from ep04.models import Post
from ep04.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']


    ## class 내에 queryset에 조건을 추가할때 사용.
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #
    #     # GET 인자에서 search 값으로 필터링
    #     # search = self.request.GET.get('search', '')
    #     # if search:
    #     #     qs = qs.filter(title__icontains=search)
    #
    #     if self.request.user.is_authenticated:
    #         qs = qs.filter(author=self.request.user)
    #     else:
    #         qs = qs.none()  # empty result
    #     qs = qs.filter(title__icontains='1')
    #     return qs