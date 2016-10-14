from random import shuffle
from django.shortcuts import render
from django.http.response import HttpResponse
from game import Game, colors

def index(request):
    return HttpResponse("<h1>Kaleido</h1>")

def all(request):
    kgame = Game()
    
    return render(request, 'kaleido/cards.html',
                  context={'cards':kgame.deck,
                           'colors':colors})

def game(request, players):
    kgame = Game()
    for _ in range(int(players)):
        kgame.newPlayer()
    
    return render(request, 'kaleido/game.html',
                  context={'game':kgame,
                           'colors':colors})
    
def cardClick(request):
    print request.POST["card"]
#    print request.POST['card']
    return HttpResponse('')