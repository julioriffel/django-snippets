#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

from django.conf import settings
from django.db import models


## START HEREANÇA


class DataAbs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(DataAbs):
    message = models.TextField(max_length=500)


class Carro(DataAbs):
    modelo = models.TextField(max_length=10)
    ano = models.IntegerField()
    portas = models.IntegerField(default=4)


# END HERANÇA

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    color = models.TextField(max_length=50, null=True)


class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'Ordinary'),
        (1, 'SuperHero'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    user_type = models.IntegerField(null=True, choices=USER_TYPES)
    bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "{}: {:.20}".format(self.user, self.bio or "")

    class Meta:
        abstract = True


class SuperHeroProfile(models.Model):
    origin = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True


class OrdinaryProfile(models.Model):
    address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


class ProfileH(SuperHeroProfile, OrdinaryProfile, BaseProfile):
    pass
