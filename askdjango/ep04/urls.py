from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'ep04'

router = DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    # path('post/', views.PostListAPIView.as_view()),
    # path('post/<int:pk>/', views.PostDetaßilAPIView.as_view()),
    path('', include(router.urls)),
]