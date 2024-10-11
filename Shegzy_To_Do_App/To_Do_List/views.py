from django.shortcuts import render, redirect
from .models import Post
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

# def home(request):
#     div_count = Post.objects.count()
#     context = {'div_count': div_count}
#     return render(request, 'To_Do_List/base.html', context)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'To_Do_List/index.html'
    ordering = ['-date_posted']

class PostCreateView(CreateView):
    model = Post
    fields = ['content']
    success_url = reverse_lazy('home')

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['content']
    success_url = reverse_lazy('home')
    paginate_by = 5
    
