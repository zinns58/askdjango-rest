from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/', views.PostListAPIView.as_view()),
]