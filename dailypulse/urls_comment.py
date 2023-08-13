from django.urls import path
from .views_comment import Create_comment,Delete_comment,Get_comment_news,Get_comment_user,Update_comment


urlpatterns = [
    path("create_comment/", Create_comment.as_view(), name="create_comment"),
    path("delete_comment/<int:pk>/", Delete_comment.as_view(), name="delete_comment"),
    path("get_comments_news/<str:title>/", Get_comment_news.as_view(), name="get_comment_news"),
    path("get_comments/<int:user_id>/", Get_comment_user.as_view(), name="Get_comment_user"),
    path("update_comment/<int:pk>/", Update_comment.as_view(), name="Update_comment"),
]
