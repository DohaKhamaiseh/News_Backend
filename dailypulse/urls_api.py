from django.urls import path
from .views_api import getNewsByCategory, getNewByLanguage, getWeather


urlpatterns = [
     path("list/<str:category>/", getNewsByCategory),
    path("list/<str:category>/<str:lang>/", getNewByLanguage),
    path("<str:location>/", getWeather),
]
