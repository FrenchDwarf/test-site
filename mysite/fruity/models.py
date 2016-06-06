from django.db import models

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length=100)

    def __str__(self):
        return self.game_name

class Probability(models.Model):
    result_name = models.CharField(max_length=100)
    weight_value = models.FloatField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.result_name + " ==> " + str(self.weight_value)

class Player(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    spin_count = models.IntegerField()
    coin_count = models.IntegerField()
    effect = models.CharField(max_length=10)
    last_round = models.CharField(max_length=10, default="None")
    is_playing = models.BooleanField(default=False)

    def __str__(self):
        return self.username
