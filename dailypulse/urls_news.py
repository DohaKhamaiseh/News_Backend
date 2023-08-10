from django.urls import path
from .views_news import CreateNewsList,GetNewsList,DeleteNews,GetNewsAllList


urlpatterns = [
    path("Create_News/", CreateNewsList.as_view(), name="Create_News"),
    path("Delete_News/<int:pk>/", DeleteNews.as_view(), name="Delete_News"),
    path("Get_News/<int:user_id>/", GetNewsList.as_view(), name="Get_News"),
    path("Get_all_News/", GetNewsAllList.as_view(), name="Get_News"),

]
