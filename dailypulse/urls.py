from django.urls import path
from .views import DailypulseList, DailypulseDetail



urlpatterns = [
    path("", DailypulseList.as_view(), name="dailypulse_list"),
    path("<int:pk>/", DailypulseDetail.as_view(), name="dailypulse_detail"),

]





