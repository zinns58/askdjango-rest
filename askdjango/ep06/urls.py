from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'ep06'

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]