# Generated by Django 4.0.4 on 2022-06-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='create_time',
            field=models.TimeField(auto_now=True, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='update_time',
            field=models.TimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=2020, verbose_name='publish year'),
        ),
    ]
