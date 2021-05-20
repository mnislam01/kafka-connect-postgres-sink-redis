from django.db import models


class Channel(models.Model):
    code = models.CharField(
        max_length=255,
        default="",
        unique=True
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )


class FreeTweet(models.Model):
    channel_code = models.CharField(
        max_length=255,
        default="",
    )
    text = models.CharField(
        max_length=1000,
        default="",
        blank=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=['channel_code']),
            models.Index(fields=["id", 'channel_code']),
        ]
