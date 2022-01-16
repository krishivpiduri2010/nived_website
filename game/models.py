from django.db import models


# Create your models here.
class Game(models.Model):
    last_login = models.IntegerField()
    money=models.IntegerField(null=True)


class Chef(models.Model):
    name = models.CharField(max_length=20)
    profitphr = models.IntegerField()
    game=models.ForeignKey(Game,models.CASCADE)


class Speciality(models.Model):
    name = models.CharField(max_length=20)
    profitpcm = models.IntegerField()
    description = models.TextField()
