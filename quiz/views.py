# coding=utf-8
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from quiz.models import Phrase
from quiz.models import PlayerRecord
from quiz.models import Set


def home_page(request):
    sets = Set.objects.all()
    response = render(request, 'home.html', {'sets': sets})
    return response


def learn_page(request):
    if request.method == 'POST':
        q_idx = int(request.POST.get('q_idx'))
        phrase = Phrase.objects.get(id=q_idx+1)
        player_record = PlayerRecord()
        player_record.phrase = phrase
        player_record.answer = request.POST.get('user_text', '')
        player_record.save()
    else:
        phrase = Phrase.objects.first()

    try:
        Phrase.objects.get(id=phrase.id + 1)
    except ObjectDoesNotExist:
        has_next_phrase = False
    else:
        has_next_phrase = True

    response = render(request, 'learn.html', {
        'quiz': phrase.korean,
        'answer': phrase.english,
        'q_idx': phrase.id,
        'has_next_phrase': has_next_phrase
        })
    return response
