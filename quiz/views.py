# coding=utf-8
from django.shortcuts import redirect, render
from django.http import HttpResponse

from quiz.models import Phrase
from quiz.models import PlayerRecord
from quiz.models import Set

def home_page(request):
    sets = Set.objects.all()
    response = render(request, 'home.html', {'sets': sets})
    return response

def learn_page(request):
    phrase = Phrase.objects.first()

    if request.method == 'POST':
        player_record = PlayerRecord()
        player_record.phrase = phrase
        player_record.answer = request.POST.get('user_text', '')
        player_record.save()

    response = render(request, 'learn.html', {
        'quiz': phrase.korean if phrase is not None else '',
        'answer': phrase.english if request.method == 'POST' else ''
        })
    return response

