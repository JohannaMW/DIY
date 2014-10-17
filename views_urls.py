import json
from django.http import HttpResponse
from django.shortcuts import render
from models import Card

def interactive(request):
    return render(request, 'interactive.html')

def get_card(request):
    cards = list(Card.objects.order_by('?'))
    user_card = cards[0]
    print user_card
    dealer_card = cards[1]
    print dealer_card
    card = { "user_card" : user_card.rank,
              "dealer_card" : dealer_card.rank }
    data = json.dumps(card)
    return HttpResponse(data, content_type='application/json')

# you still have to write the evaluation and storing of wins/loss'
def result(request):
    pass

#this goes into you urls.py
  url(r'^interactive/$', 'cards.views.interactive', name='interactive'),
  url(r'^get_card/$', 'cards.views.get_card', name='get_card'),