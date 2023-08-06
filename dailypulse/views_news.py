from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView

)

from .models import News
from .permissions import IsOwnerOrReadOnly
from .serializers import NewsSerializer
