from django.urls import path
from .views_news import CreateNewsList,GetNewsList,DeleteNews


urlpatterns = [
    path("Create_News/", CreateNewsList.as_view(), name="Create_News"),
    path("Delete_News/<int:news_id>/", DeleteNews.as_view(), name="Delete_News"),
    path("Get_News/<int:user_id>/", GetNewsList.as_view(), name="Get_News"),

]
