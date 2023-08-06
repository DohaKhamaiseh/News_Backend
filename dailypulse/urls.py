from django.urls import path
from .views import DailypulseList, DailypulseDetail
from .views import CreateReadingList, DeleteReadingList, GetReadingList


urlpatterns = [
    path("", DailypulseList.as_view(), name="dailypulse_list"),
    path("<int:pk>/", DailypulseDetail.as_view(), name="dailypulse_detail"),
    path("readinglist/", CreateReadingList.as_view(), name="readinglist_create"),
    path("readinglist/<int:pk>/", DeleteReadingList.as_view(), name="readinglist_delete"),
    path("readinglistget/<int:user_id>/", GetReadingList.as_view(), name="readinglist_get"),

]


# test create reading list : http://127.0.0.1:8000/api/v1/dailypulse/readinglist/
# method:POST
# body :
#  {
#   "url":"amer",
#   "title": "amjad",
#   "source": "sjsjs",
#   "author": "hhhfhfhf",
#   "url_image": "https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/SAA_logo_%282019%29.svg/1200px-SAA_logo_%282019%29.svg.png",
#   "published_date": "2222-07-15",
#   "description":"hdhdh",
#   "content": "amamama",
#   "user":1

# }

# test delete reading list : http://127.0.0.1:8000/api/v1/dailypulse/readinglist/<id>
# method:DELETE

# test get reading list : http://127.0.0.1:8000/api/v1/dailypulse/readinglistget/<user_id>
# method:GET


