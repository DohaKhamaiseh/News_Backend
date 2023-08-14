from django.urls import path
# from .views import SignUpView
from accounts import views
from .views import Update_user
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("update_user/<int:pk>/", Update_user.as_view(), name="Update_comment"),
]
