from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from . import views

urlpatterns = [
    # path('', views.TaskListView, name='home')
    path('', TaskListView.as_view(), name='home'),
    path('task/<int:pk>/detail/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('new/task/', TaskCreateView.as_view(), name='new_task'),
]

