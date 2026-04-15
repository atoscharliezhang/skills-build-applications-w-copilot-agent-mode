from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeaderboardEntryViewSet

router = DefaultRouter()
router.register(r'leaderboard', LeaderboardEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]