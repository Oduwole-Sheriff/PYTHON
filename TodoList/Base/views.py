from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Base.models import Task
from Base.serializers import TaskSerializer, LoginSerializer, RegisterSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from rest_framework.response import Response

from rest_framework.views import APIView
 
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.

# def PostListView(request):
#     return render(request, 'Base/home.html')

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        print(serializer.data)
        user = authenticate(username = serializer.data['username'], password = serializer.data['password'])
        if not user:
            return Response({
                'status': False,
                'message': "invalid credentials"
            }, status.HTTP_400_BAD_REQUEST)

        token = Token.objects.get_or_create(user=user)
        print(token)
        return Response({'status': True, 'message': 'user login', 'token': str(token) }, status.HTTP_201_CREATED)


class ResgisterAPI(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data = data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        
        return Response({'status': True, 'message': 'user created'}, status.HTTP_201_CREATED)

class PersonView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        objs = Task.objects.all()
        serializer = TaskSerializer(objs, many = True)
        print(serializer.data)
        return Response(serializer.data)
        # return Response({'message': "this is a GET request"})

    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
        # return Response({'message': "this is a POST request"})
    
    def put(self, request):
        data = request.data
        serializer = TaskSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message': "this is a PUT request"})

    def patch(self, request):
        data = request.data
        serializer = TaskSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message': "this is a Patch request"})

    def delete(self, request):
        data = request.data
        objs = Task.objects.get(id = data['id'])
        objs.delete()
        return Response({'message' : 'person deleted'})

class TaskListView(ListView):
    model = Task
    template_name = 'Base/home.html'
    context_object_name = 'tasks'
    ordering = ['-date_posted']

    def get_queryset(self):
        return Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        completed_tasks = Task.objects.filter(complete=True)
        uncompleted_tasks = Task.objects.filter(complete=False)
        context['completed_tasks'] = completed_tasks.count
        context['uncompleted_tasks'] = uncompleted_tasks
        context['total_tasks'] = self.get_queryset().count()
        return context


class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['content', 'complete']
    template_name = 'Base/task_form.html'
    success_url = reverse_lazy('home')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['content', 'complete']
    # success_url = reverse_lazy('home')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

    def test_func(self):
        # Implement your authorization logic here
        # For example, if you want to allow only the creator of the task to update it:
        task = self.get_object()
        return self.request.user == task.creator

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'
