# from django.shortcuts import render

# # Create your views here.

# from django.shortcuts import render
# from .forms import CityForm

# import requests

# def weather_view(request):
#     form = CityForm()
#     weather_data = None

#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         if form.is_valid():
#             city = form.cleaned_data['city']
#             # Replace 'YOUR_API_KEY' with your actual API key
#             response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY')
#             weather_data = response.json()

#     return render(request, 'weather/weather.html', {'form': form, 'weather_data': weather_data})


# from django.shortcuts import render
# from .forms import CityForm
# import requests

# def weather_view(request):
#     form = CityForm()
#     weather_data = None

#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         if form.is_valid():
#             city = form.cleaned_data['city']
#             # Replace 'YOUR_API_KEY' with your actual API key
#             response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY')
#             weather_data = response.json()

#     return render(request, 'weather/weather.html', {'form': form, 'weather_data': weather_data})


import requests
from django.shortcuts import render
from .forms import CityForm

def weather_view(request):
    form = CityForm()
    weather_data = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            # Replace 'YOUR_API_KEY' with your actual API key
            response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=266686c4d633ee17a8b1c352e1319d11&units=metric')
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {'error': 'Failed to retrieve data'}

    return render(request, 'weather/weather.html', {'form': form, 'weather_data': weather_data})
