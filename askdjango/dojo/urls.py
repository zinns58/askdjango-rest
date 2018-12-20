from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'dojo'

router = DefaultRouter()
router.register(r'post', views.PostViewSet) # 2개의 URL을 처리하는 뷰함수를 만들어서 등록

urlpatterns = [
    path('', include(router.urls)),
]