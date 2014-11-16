# coding=utf-8
from django.shortcuts import render

from quiz.models import Phrase
from quiz.models import PlayerRecord
from quiz.models import Set


def home_page(request):
    sets = Set.objects.all()
    response = render(request, 'home.html', {'sets': sets})
    return response


def learn_page(request, set_name):
    set_ = Set.objects.get(name__exact=set_name)
    if request.method == 'POST':
        q_idx = int(request.POST.get('q_idx'))
        phrase = Phrase.objects.filter(set_id=set_.id).\
            order_by('pk').filter(id__gt=q_idx)[0]
        player_record = PlayerRecord()
        player_record.phrase = phrase
        player_record.answer = request.POST.get('user_text', '')
        player_record.save()
    else:
        phrase = Phrase.objects.filter(set=set_).order_by('pk')[0]

    next_phrase = Phrase.objects.filter(set_id=set_.id).\
        order_by('pk').filter(id__gt=phrase.id)
    has_next_phrase = False if len(next_phrase) == 0 else True

    response = render(request, 'learn.html', {
        'set': set_,
        'quiz': phrase.korean,
        'answer': phrase.english,
        'q_idx': phrase.id,
        'has_next_phrase': has_next_phrase
        })
    return response
