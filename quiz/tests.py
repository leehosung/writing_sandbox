# coding=utf-8
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.shortcuts import render

from quiz.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode('utf-8'), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['user_text'] = 'I have question'
        response = home_page(request)
        expected_html = render_to_string(
            'home.html',
            {'answer': 'I have question'}
        )
        self.assertEqual(response.content.decode('utf-8'), expected_html)
