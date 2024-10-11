from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=18a2a40d412fd9b32241c23d365816f6').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon'])+ ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp'])+'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']), 
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
