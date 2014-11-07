# coding=utf-8
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.shortcuts import render

from quiz.views import home_page
from quiz.models import Phrase
from quiz.models import PlayerRecord


class HomePageTest(TestCase):

    def setUp(self):
        phrase = Phrase()
        phrase.url = "http://www.stackoverflow.com"
        phrase.english = "I have a question"
        phrase.korean = "질문이 있어요"
        phrase.category = "QnA"
        phrase.save()

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string(
            'home.html', {
                'quiz': '질문이 있어요',
            })
        self.assertEqual(response.content.decode('utf-8'), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['user_text'] = 'I have question'
        response = home_page(request)

        self.assertEqual(PlayerRecord.objects.count(), 1)
        player_record = PlayerRecord.objects.first()
        self.assertEqual(player_record.answer, "I have question")

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(PlayerRecord.objects.count(), 0)

    def test_home_page_can_show_a_answer_after_user_input(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['user_text'] = 'I have question'
        response = home_page(request)

        expected_html = render_to_string("home.html", {
            'quiz': '질문이 있어요',
            'answer': 'I have a question'})
        self.assertEqual(response.content.decode('utf-8'), expected_html)


class PhraseModelTest(TestCase):
    
    def test_saving_and_retreiving_phrases(self):
        first_phrase = Phrase()
        first_phrase.url = "http://www.stackoverflow.com"
        first_phrase.english = "I have a question"
        first_phrase.korean = "질문이 있어요"
        first_phrase.category = "QnA"
        first_phrase.save()

        second_phrase = Phrase()
        second_phrase.url = "http://www.github.com"
        second_phrase.english = "Is it possible to transfer Wiki content to another's repository?"
        second_phrase.korean = "위키를 다른 사람의 저장소로 옮길 수 있을까요?"
        second_phrase.category = "Issue"
        second_phrase.save()

        saved_phrases = Phrase.objects.all()
        self.assertEqual(saved_phrases.count(), 2)

        first_saved_phrase = saved_phrases[0]
        second_saved_phrase = saved_phrases[1]

        self.assertEqual(first_saved_phrase.category, "QnA")
        self.assertEqual(second_saved_phrase.category, "Issue")

class PlayerRecordTest(TestCase):

    def test_saving_and_retreiving_player_record(self):
        phrase = Phrase()
        phrase.url = "http://www.stackoverflow.com"
        phrase.english = "I have a question"
        phrase.korean = "질문이 있어요"
        phrase.category = "QnA"
        phrase.save()

        player_record = PlayerRecord()
        player_record.phrase = phrase
        player_record.answer = "I have question"
        player_record.save()

        saved_player_records = PlayerRecord.objects.all()
        self.assertEqual(saved_player_records.count(), 1)

        saved_player_record = saved_player_records[0]

        self.assertEqual(saved_player_record.answer, "I have question")
