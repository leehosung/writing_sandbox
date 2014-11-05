# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    response = render(request, 'home.html',
        {'answer': request.POST.get('user_text', '')}
        )
    return response

