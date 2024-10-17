from django.shortcuts import render
from .models import Book
from .forms import PostSearchForm
# Create your views here.

def post_search(request):
    form  = PostSearchForm

    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            
            results = Book.objects.filter(title__contains=q)
            # results = Book.objects.filter(title__icontains=q)
            # results = Book.objects.filter(title__search=q)

            # from django.contrib.postgres.search import SearchVector
            # results = Book.objects.annotate(search=SearchVector('title', 'authors'),).filter(search=q)

    return render(request, 'index.html', {"form":form, 'results':results})