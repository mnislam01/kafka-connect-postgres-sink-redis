from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    tweet = serializers.CharField()
