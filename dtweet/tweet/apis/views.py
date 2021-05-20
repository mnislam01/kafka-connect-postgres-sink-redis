from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from tweet.models import (
    Channel,
    FreeTweet
)

from tweet.apis.serializers import (
    ChannelSerializer,
    FreeTweetSerializer
)


class ChannelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class FreeTweetViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = FreeTweet.objects.all()
    serializer_class = FreeTweetSerializer
