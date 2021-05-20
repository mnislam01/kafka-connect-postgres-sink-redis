from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from dredis.apis.serializers import TweetSerializer
from dredis.services import conn_service


class DefaultTweetPagination(LimitOffsetPagination):
    default_limit = 30


class TweetStreamAPIView(ListAPIView):
    permission_classes = [AllowAny]
    pagination_class = DefaultTweetPagination
    serializer_class = TweetSerializer

    def get_queryset(self):
        tweets = []
        client = conn_service.get_client()
        data = client.get(self.kwargs["channel"])
        if data:
            tweets = data
        return tweets
