from django.urls import path, include
from blog.views import PostViewApi, LoginAPI, ResgisterAPI

urlpatterns = [
    path('post/', PostViewApi.as_view()),
    path('login/', LoginAPI.as_view()),
    path('register/', ResgisterAPI.as_view()),
]