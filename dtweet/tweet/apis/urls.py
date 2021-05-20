from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tweet.apis import views


router = DefaultRouter()
router.register('channels', views.ChannelViewSet)
router.register(r'tweets', views.FreeTweetViewSet)

app_name = "tweet"

urlpatterns = [
    path('', include(router.urls)),
]
