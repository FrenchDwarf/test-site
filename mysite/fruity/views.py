from django.shortcuts import render, get_object_or_404
import random

# from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse

from .models import Game, Player, Probability

# Create your views here.

def index(request):
    five_games = Game.objects.order_by("-game_name")[:5]
    context = {"games": five_games}
    return render(request, "fruity/index.html", context)

def gamesummary(request, name_of_game):
    game = get_object_or_404(Game, game_name=name_of_game)
    return render(request, "fruity/gamesummary.html", {"game": game})

def game(request, name_of_game, username):
    game = get_object_or_404(Game, game_name=name_of_game)
    player = get_object_or_404(Player, username=username)
    if request.POST.get("result"):
        player.last_round = spin_the_wheel(game)
        player.is_playing = True
        player.spin_count -= 1

        if player.last_round == "Swarm" or player.last_round == "SlowMo" or player.last_round == "Shield":
            player.effect = player.last_round
        else:
            player.effect = "None"

            if player.last_round == "1 x Spin":
                player.spin_count += 1
            elif player.last_round == "2 x Spin":
                player.spin_count += 2
            elif player.last_round == "3 x Spin":
                player.spin_count += 3
            elif player.last_round == "1 x Coin":
                player.coin_count += 1
            elif player.last_round == "2 x Coin":
                player.coin_count += 2
            elif player.last_round == "3 x Coin":
                player.coin_count += 3
            elif player.last_round == "Jackpot":
                player.coin_count += 50

        player.save()
        return render(request, "fruity/game.html", {"game": game, "player": player})
    else:
        player.is_playing = False

        # Because no buying functionality, reset on first play
        player.coin_count = 0
        player.spin_count = 50
        # Because no buying functionality, reset on first play

        player.save()
        return render(request, "fruity/game.html", {"game": game, "player": player})


def spin_the_wheel(game):
    allweights = Probability.objects.filter(game=game)

    totalweight = 0
    for weight in allweights:
        totalweight += weight.weight_value

    rand = random.random() * totalweight

    total = 0

    for prob in allweights:
        total += prob.weight_value
        if rand <= total:
            return prob.result_name

    return "Lose"
