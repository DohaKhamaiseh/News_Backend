from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

from .forms import CustomUserCreationForm
import json
from django.http import JsonResponse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    UpdateAPIView

)

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@csrf_exempt
def signup(request):
    res = json.loads(request.body)
    user = CustomUser.objects.create(
        username=res['username'],
      email=res['email'],
      first_name=res['first_name'],
      last_name=res['last_name'],
      location = res['location']
    )
    user.set_password(res['password1'])
    user.save()
    return JsonResponse({"message":"success"})


class Update_user(UpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def update(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        body = json.loads(request.body)
        rowtobeupdated = CustomUser.objects.get(id = pk)
        rowtobeupdated.email= body['email']
        rowtobeupdated.first_name= body['first_name']
        rowtobeupdated.last_name= body['last_name']
        rowtobeupdated.location = body['location']
        rowtobeupdated.save()
        remaining_data = CustomUser.objects.filter(id=pk)  # Retrieve the remaining data
        serializer = self.get_serializer(remaining_data, many=True)

        return Response(serializer.data)

# class Update_user(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
