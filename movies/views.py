from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    
    filterset_fields = ['director__name', 'actors__name', 'genres__name']
    ordering_fields = ['name', 'year_of_release', 'user_rating']
    search_fields = ['name', 'director__name', 'actors__name', 'genres__name']

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(detail=True, methods=['delete'], url_path='delete-if-not-associated')
    def delete_if_not_associated(self, request, pk=None):
        actor = get_object_or_404(Actor, pk=pk)
        if actor.movies.exists():
            return Response({"error": "Actor is associated with movies, cannot be deleted."}, status=status.HTTP_400_BAD_REQUEST)
        
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    