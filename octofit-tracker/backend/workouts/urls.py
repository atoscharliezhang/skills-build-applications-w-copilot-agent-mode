from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutSuggestionViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutSuggestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]