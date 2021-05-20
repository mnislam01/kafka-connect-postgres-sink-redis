from django.urls import path, include

from dredis.apis.views import TweetStreamAPIView

app_name = "dredis"

urlpatterns = [
    path('<str:channel>/', TweetStreamAPIView.as_view(), name="dredis-tweets"),
]
