from django.contrib import admin

# Register your models here.
from .models import Game, Probability, Player

admin.site.register(Game)
admin.site.register(Probability)
admin.site.register(Player)