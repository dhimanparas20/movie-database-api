from django.db import models

ACTION = 'AC'
COMEDY = 'CO'
DRAMA = 'DR'
HORROR = 'HO'
ROMANCE = 'RO'
SCIFI = 'SF'
FANTASY = 'FA'
THRILLER = 'TH'

GENRE_CHOICES = [
    (ACTION, 'Action'),
    (COMEDY, 'Comedy'),
    (DRAMA, 'Drama'),
    (HORROR, 'Horror'),
    (ROMANCE, 'Romance'),
    (SCIFI, 'Sci-Fi'),
    (FANTASY, 'Fantasy'),
    (THRILLER, 'Thriller'),
]

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Technician(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.role})"

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year_of_release = models.IntegerField()
    user_rating = models.FloatField()
    genres = models.CharField(choices=GENRE_CHOICES,default=ACTION,max_length=100)
    actors = models.ManyToManyField(Actor, related_name='movies')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    technicians = models.ManyToManyField(Technician, related_name='movies')

    def __str__(self):
        return self.name
