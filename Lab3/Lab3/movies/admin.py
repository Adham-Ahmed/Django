from django.contrib import admin
from attr import field
from movies.models import Movie

# Register your models here.
# admin.site.register(Actor)
@admin.register(Movie)
class actorAdmin(admin.ModelAdmin):
    list_display = ['name','year']
    search_fields= ['name']
    list_filter= ['year']
    