import os
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


# API ROUTES :

# route to get data require a category(q)
@api_view(['GET'])
def getNewsByCategory(request, category):

    APIKey = os.getenv('API_KEY_News')
    url = 'https://newsapi.org/v2/everything?q={cat}&apiKey={key}'.format(cat=category,key=APIKey)
    response = requests.get(url)

    if response.status_code == 200:
         data = response.json()

         return Response(data)
    else:
            return Response({'message': 'Failed to fetch news information from the API'})

# route to get arabic news require a category(q)
@api_view(['GET'])
def getNewByLanguage(request, lang, category):
    APIKey = os.getenv('API_KEY_News')
    url = 'https://newsapi.org/v2/everything?q={cat}&language={lang}&apiKey={key}'.format(cat=category,lang=lang,key=APIKey)
    response = requests.get(url)

    if response.status_code == 200:
         data = response.json()

         return Response(data)
    else:
            return Response({'message': 'Failed to fetch news information from the API'})


# weather route link 'http://api.openweathermap.org/data/2.5/weather?q=LOCATION&appid=f22892654725839a44ff6db985f0b151' require the user ocation in url
@api_view(['GET'])
def getWeather(request,location):
    APIKey = os.getenv('API_KEY_Weather')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={loc}&apiKey={key}'.format(loc=location,key=APIKey)
    response = requests.get(url)

    if response.status_code == 200:
         data = response.json()

         return Response(data)
    else:
            return Response({'message': 'Failed to fetch news information from the API'})
