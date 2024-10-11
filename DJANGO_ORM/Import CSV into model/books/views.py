from django.shortcuts import render
from django.db.models import Sum
from .models import Book

# Create your views here.
def example(request):
    data = Book.objects.all().aggregate(data=Sum('ratings_count'))
    print(data)
    return render(request, 'index.html', {'data':data})