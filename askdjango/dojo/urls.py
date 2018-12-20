from django.urls import path
from . import views


app_name = 'dojo'

urlpatterns = [
    path('post', views.post_list),
]