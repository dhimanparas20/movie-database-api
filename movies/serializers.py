from rest_framework import serializers
from .models import Movie, Actor, Director, Technician

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    director = DirectorSerializer(read_only=True)
    technicians = TechnicianSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
