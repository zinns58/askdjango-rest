from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet


app_name = 'ep15'

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]