from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Dailypulse,News
from .permissions import IsOwnerOrReadOnly
from .serializers import DailypulseSerializer,NewsSerializer
import json
from django.http import JsonResponse


class DailypulseList(ListCreateAPIView):
    queryset = Dailypulse.objects.all()
    serializer_class = DailypulseSerializer


class DailypulseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Dailypulse.objects.all()
    serializer_class = DailypulseSerializer


# create reading list : body attributes  all exepet id
# delete reading list : requeiring id in url
# get reading list : requiring user id in url

# create comment : body attributes all
# delete comment : comment id url
# get comment : requeering user id and news id in url
# get comments : requeering news id in url
# update comment : comment id url ,body description

# create News : body attributes all
def Create_News(request):
    res = json.loads(request.body)
    new = News.objects.create(
        source=res['source'],
      author=res['author'],
      title=res['title'],
      description=res['description'],
      url = res['url'],
      url_image = res['url_image'],
      published_date = res['published_date'],
      content = res['content']
    )
    # user.set_password(res['password1'])
    # new.save()
    return JsonResponse(list(new),safe=False)


# get news : requering user id in url
# delete news : requeiring news id

# API ROUTES :
# route to get data require a category(q)
# route to get arabic news require a category(q)
# weather route link 'http://api.openweathermap.org/data/2.5/weather?q=LOCATION&appid=f22892654725839a44ff6db985f0b151' require the user ocation in url


# get USER info : user id url
# update USER : user id url , body attributes all
