import datetime
from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
# Create your views here.
def ConvertTime(dt_utc,tdelta):
    return datetime.datetime.utcfromtimestamp(dt_utc) + datetime.timedelta(seconds=tdelta)

def index(request):
    # API key goes here
    key=''
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city,key)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist!'
            else:
                err_msg = 'City already exists!'
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added Successfully!'
            message_class = 'is_success'
    
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city,key)).json()
        city_weather = {
            'city' : city.name,
            'country': r['sys']['country'],
            'temperature' : round(r['main']['temp'] - 273.15,2),
            'time': ConvertTime(r['dt'],r['timezone']),
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    context = {
        'weather_data' : weather_data, 
        'form' : form,
        'message' : message,
        'message_class' : message_class
        }
    return render(request,'weather/weather.html', context)
def delete_city(requests, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
