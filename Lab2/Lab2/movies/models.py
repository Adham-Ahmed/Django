from django.db import models
# from actors.models import Actor


# Create your models here.

class Movie(models.Model):
    name = models.fields.CharField(verbose_name='movie', max_length=25, unique=True)
    year = models.fields.IntegerField(verbose_name='publish year',default=2020)
    actors = models.ManyToManyField('actors.actor')
    director = models.CharField(max_length=50, default='')
    create_time = models.TimeField(verbose_name='Created at', auto_now=True)
    update_time = models.TimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f'{self.name}'