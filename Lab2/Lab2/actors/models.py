from django.db import models

#from movies.models import Movie

GENDER_LIST = [('male', 'male'), ('female', 'female')]


# Create your models here.
class Actor(models.Model):
    name = models.fields.CharField(verbose_name='Name', max_length=25, unique=True)
    gender = models.CharField(verbose_name='Gender', choices=GENDER_LIST, max_length=6,default='male')
    age = models.IntegerField(default=0)
    # movies = models.ManyToManyField('movies.movie')
    create_time = models.TimeField(verbose_name='Created at', auto_now=True)
    update_time = models.TimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f'{self.name}'
