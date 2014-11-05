# coding=utf-8
from django.shortcuts import redirect, render
from django.http import HttpResponse

from quiz.models import Phrase
from quiz.models import PlayerRecord


def home_page(request):
    phrase = Phrase.objects.first()

    if request.method == 'POST':
        player_record = PlayerRecord()
        player_record.phrase = phrase
        player_record.answer = request.POST.get('user_text', '')
        player_record.save()
        return redirect('/')

    response = render(request, 'home.html', {
        'quiz': phrase.korean,
        'answer': phrase.english
        })
    return response

