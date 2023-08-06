from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Dailypulse , Reading_later
from .permissions import IsOwnerOrReadOnly
from .serializers import DailypulseSerializer , ReadingLaterSerializer


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
# get news : requering user id in url
# delete news : requeiring news id

# API ROUTES :
# route to get data require a category(q)
# route to get arabic news require a category(q)
# weather route link 'http://api.openweathermap.org/data/2.5/weather?q=LOCATION&appid=f22892654725839a44ff6db985f0b151' require the user ocation in url


# get USER info : user id url
# update USER : user id url , body attributes all

class CreateReadingList(ListCreateAPIView):
    '''
    create reading list : body attributes  all exepet id
    '''
    queryset = Reading_later.objects.all()
    serializer_class = ReadingLaterSerializer

class DeleteReadingList(RetrieveUpdateDestroyAPIView):
    '''
    delete reading list : requeiring id in url
    '''
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Reading_later.objects.all()
    serializer_class = ReadingLaterSerializer

class GetReadingList(ListCreateAPIView):
    '''
    get reading list : requiring user id in url
    '''
    queryset = Reading_later.objects.all()
    serializer_class = ReadingLaterSerializer

    