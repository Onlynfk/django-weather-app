import  requests
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm

# Create your views here.
def home_view (request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d697a11cfb37def5c7b1dc094cca8fd1'
    # city = 'Port Harcourt'

    #print(req.text)
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()   # reset the signal
    
    cities = City.objects.all()
    
    data_of_weather = []
    
    for city in cities:
        
        req = requests.get(url.format(city)).json()
        

        weather_in_city = {
            'city': city.name,
            'temperature': req['main']['temp'],
            'description': req['weather'][0]['description'],
            'icon': req['weather'][0]['icon'],
            'country': req['sys']['country'],
            'lon': req['coord']['lon'],
            'lat': req['coord']['lat'],
        }
        
        data_of_weather.append(weather_in_city)

        
        #print(data_of_weather)
        
    context = {
            'data_of_weather': data_of_weather,
            'form': form,
        }   
    return render(request, template_name='weather/weather.html', context= context)


def deleteAll(request):
    City.objects.all().delete()
    return redirect('home')