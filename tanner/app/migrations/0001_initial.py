# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 22:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name=b'nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name=b'nombre')),
                ('slug', models.SlugField(verbose_name=b'ruta')),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='pages',
            field=models.ManyToManyField(to='app.Page'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
