from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

from .forms import CustomUserCreationForm
import json
from django.http import JsonResponse

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
