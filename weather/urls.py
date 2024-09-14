# from django.urls import path
# from .views import weather_view

# urlpatterns = [
#     path('weather/', weather_view, name='weather'),
# ]


from django.urls import path
from .views import weather_view

urlpatterns = [
    path('', weather_view, name='weather'),  # This sets up the root URL for this app
]
