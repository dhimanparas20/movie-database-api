from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet,ActorViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'actors', ActorViewSet, basename='actor')

# URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
