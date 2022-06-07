from django.contrib import admin
from attr import field
from actors.models import Actor

# Register your models here.
# admin.site.register(Actor)
@admin.register(Actor)
class actorAdmin(admin.ModelAdmin):
    list_display = ['name','gender','age']
    search_fields= ['name']
    list_filter= ['gender']
    fieldsets = (
          ('Name Section',{'fields':['name']})
          ,
          ('Gender Section',{'fields':['gender']})
    )
    