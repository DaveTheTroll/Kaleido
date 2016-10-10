from random import shuffle
from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return HttpResponse("<h1>Kaleido</h1>")

def all(request):
    colors = ('WHITE', 'RED', 'GREEN', 'BLACK', 'BLUE')
    cards = [{'bg':bg, 'fg':fg, 'txt':txt} for bg in colors \
                for fg in colors \
                for txt in colors \
                if fg != bg]
    shuffle(cards)
    
    return render(request, 'kaleido/cards.html',
                  context={'cards':cards,
                           'colors':colors})