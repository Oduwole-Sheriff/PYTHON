from django.shortcuts import render
from django.db.models import Sum, Min, Max, Avg
from .models import Books
from django.views.generic import ListView

# Create your views here.
# def example(request):
#     data = Books.objects.aggregate(sum=Sum('ratings_count'), max=Max('ratings_count'), min=Min('ratings_count'), avg=Avg('ratings_count'))

#     return render(request, 'index.html', {'data': data})

class Example(ListView):
    model = Books
    template_name = 'index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(Example, self).get_context_data(*args, **kwargs)
        context['ratings_count'] = Books.objects.aggregate(Sum('ratings_count'))
        return context

# def example(request):
#     _sum = Books.objects.aggregate(sum=Sum('ratings_count'))
#     _max = Books.objects.aggregate(max=Max('ratings_count'))
#     _min = Books.objects.aggregate(min=Min('ratings_count'))
#     _avg = Books.objects.aggregate(avg=Avg('ratings_count'))
#     return render(request, 'index.html', {'sum': _sum, 'max': _max, 'min': _min, 'avg': _avg})