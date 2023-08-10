from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView

)
from rest_framework.permissions import IsAuthenticated
from .models import News
from .permissions import IsOwnerOrReadOnly
from .serializers import NewsSerializer
from rest_framework.response import Response
import json


# create News : body attributes all
class CreateNewsList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# get news : requering user id in url
class GetNewsList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NewsSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return News.objects.filter(user_id=user_id)

# delete news : requeiring news id
class DeleteNews(DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        remaining_data = News.objects.all()
        serializer = self.get_serializer(remaining_data, many=True)

        return Response(serializer.data)

class GetNewsAllList(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
