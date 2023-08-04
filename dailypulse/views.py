from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Dailypulse
from .permissions import IsOwnerOrReadOnly
from .serializers import DailypulseSerializer


class DailypulseList(ListCreateAPIView):
    queryset = Dailypulse.objects.all()
    serializer_class = DailypulseSerializer


class DailypulseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Dailypulse.objects.all()
    serializer_class = DailypulseSerializer

