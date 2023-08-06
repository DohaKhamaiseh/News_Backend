from django.urls import path
from .views import DailypulseList, DailypulseDetail,Create_News


urlpatterns = [
    path("", DailypulseList.as_view(), name="dailypulse_list"),
    path("<int:pk>/", DailypulseDetail.as_view(), name="dailypulse_detail"),
    path("Create_News/", Create_News),

]
