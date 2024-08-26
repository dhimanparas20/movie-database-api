from django.contrib import admin
from .models import *

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    # list_filter = ['short_url','long_url']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    # list_filter = ['short_url','long_url']    

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    search_fields = ['name','role']
    list_display = ['name','role']
    # list_filter = ['name','role']    

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    search_fields = ['name','year_of_release','user_rating','genres','actors','director','technicians']
    list_display =  ['name','year_of_release']
    list_filter = ['year_of_release','genres']        