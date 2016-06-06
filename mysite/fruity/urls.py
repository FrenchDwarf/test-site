from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r"^(?P<name_of_game>\w+)/$", views.gamesummary, name="gamesummary"),
    url(r"^(?P<name_of_game>\w+)/(?P<username>\w+)/$", views.game, name="game"),
]