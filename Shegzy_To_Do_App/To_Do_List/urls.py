from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('add/new/', PostCreateView.as_view(), name='add-post'),
    path('delete/<int:pk>/post', PostDeleteView.as_view(), name='delete-post'),
    path('update/<int:pk>/post', PostUpdateView.as_view(), name='update-post'),
]