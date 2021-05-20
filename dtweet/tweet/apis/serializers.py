from rest_framework import serializers

from tweet.models import (
    Channel,
    FreeTweet
)


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"


class FreeTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeTweet
        fields = "__all__"
