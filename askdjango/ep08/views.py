import time
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from django.core.signals import request_started, request_finished
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .permissions import IsAuthorUpdateOrReadonly
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (
    #     IsAuthorUpdateOrReadonly,
    # )

    # perform_ 계열 함수를 통해, API 수행 결과를 DB에 반영하는 create/update/destroy 함수를 커스텀
    # serializer.save 함수에 키워드 인자를 함께 DB 에 적용
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            ip=self.request.META['REMOTE_ADDR']
        )

    def dispatch(self, request, *args, **kwargs):
        global cbv
        cbv = self

        dispatch_start = time.time()
        response = super().dispatch(request, *args, **kwargs)

        render_start = time.time()
        # response.render()
        self.render_time = time.time() - render_start

        self.dispatch_time = time.time() - dispatch_start
        self.api_view_time = self.dispatch_time - (self.render_time + self.serializer_time + self.db_time)

        return response

    def list(self, request, *args, **kwargs):
        db_start = time.time()

        data = cache.get('post_list_cache')
        if data is None:
            data = list(self.queryset.values('author__username', 'message'))
            cache.set('post_list_cache', data)

        self.db_time = time.time() - db_start

        self.serializer_time = 0

        return HttpResponse(json.dumps(data), content_type='application/json; charset=utf-8')


def started_fn(sender, **kwargs):
    global started
    started = time.time()

def finished_fn(sender, **kwargs):
    request_response_time = (time.time() - started) - cbv.dispatch_time

    total = cbv.db_time + cbv.serializer_time + cbv.api_view_time + cbv.render_time + request_response_time

    print('Total                            : {:.6f}s'.format(total))
    print('Database Lookup - db_time        : {:.6f}s, {:>4.1f}%'.format(cbv.db_time, 100 * (cbv.db_time / total)))
    print('Serializer - serializer_time     : {:.6f}s, {:>4.1f}%'.format(cbv.serializer_time, 100 * (cbv.serializer_time / total)))
    print('API View - api_view_time         : {:.6f}s, {:>4.1f}%'.format(cbv.api_view_time, 100 * (cbv.api_view_time / total)))
    print('Response rendering - render_time : {:.6f}s, {:>4.1f}%'.format(cbv.render_time, 100 * (cbv.render_time / total)))
    print('Django request/response          : {:.6f}s, {:>4.1f}%'.format(request_response_time, 100 * (request_response_time / total)))

# request_started.connect(started_fn)
# request_finished.connect(finished_fn)