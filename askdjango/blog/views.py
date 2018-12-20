from django.contrib.auth import get_user_model
# from django.shortcuts import get_object_or_404
# from rest_framework import generics
# from rest_framework import mixins
from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer, UserSerializer


# STEP #1 : APIView 를 상속받아서 구현
# class PostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#
#
# # /post/10/ => GET, PUT, DELETE
# class PostDetailAPIView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Post, pk=pk)
#
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
#
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=204)


# STEP #2 : mixins 을 상속받아서 구현
# class PostListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,
#                       generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, reqeust, *args, **kwargs):
#         return self.list(reqeust, *args, **kwargs)
#
#     def post(self, request, reqeust, *args, **kwargs):
#         return self.create(reqeust, *args, **kwargs)
#
#
# class PostDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, reqeust, *args, **kwargs):
#         return self.retrieve(reqeust, *args, **kwargs)
#
#     def put(self, reqeust, *args, **kwargs):
#         return self.update(reqeust, *args, **kwargs)
#
#     def delete(self, reqeust, *args, **kwargs):
#         return self.destory(reqeust, *args, **kwargs)


# STEP #3 : generics 를 상속해서 구현
# class PostListAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# STEP #4 : Viewset 을 이용한 구현
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer