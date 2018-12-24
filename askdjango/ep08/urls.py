from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'ep08'

router = DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
