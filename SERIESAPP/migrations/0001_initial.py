# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparicion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('titulo', models.CharField(max_length=300)),
                ('serie', models.CharField(max_length=300)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
                ('pais', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=300)),
                ('edad', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Rodaje',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('capitulo', models.ForeignKey(to='SERIESAPP.Capitulo')),
                ('localidad', models.ForeignKey(to='SERIESAPP.Localidad')),
            ],
        ),
        migrations.AddField(
            model_name='capitulo',
            name='localidades',
            field=models.ManyToManyField(to='SERIESAPP.Localidad', through='SERIESAPP.Rodaje'),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='personajes',
            field=models.ManyToManyField(to='SERIESAPP.Personaje', through='SERIESAPP.Aparicion'),
        ),
        migrations.AddField(
            model_name='aparicion',
            name='capitulo',
            field=models.ForeignKey(to='SERIESAPP.Capitulo'),
        ),
        migrations.AddField(
            model_name='aparicion',
            name='personaje',
            field=models.ForeignKey(to='SERIESAPP.Personaje'),
        ),
    ]
