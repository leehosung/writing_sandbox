# coding=utf-8
from django.core.urlresolvers import resolve
from django.test import TestCase

from quiz.views import home_page
from quiz.views import learn_page
from quiz.models import PlayerRecord
from quiz.models import Set


class HomePageTest(TestCase):

    fixtures = ['quiz/fixtures/test.json']

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_show_set_list(self):
        Set.objects.create(name="QnA")
        response = self.client.get('/')
        self.assertContains(response, 'QnA')


class LearnPageTest(TestCase):

    fixtures = ['quiz/fixtures/test.json']

    def test_root_url_resolves_to_learn_page_view(self):
        found = resolve('/sets/QnA/learn')
        self.assertEqual(found.func, learn_page)

    def test_uses_learm_template(self):
        response = self.client.get('/sets/QnA/learn')
        self.assertTemplateUsed(response, 'learn.html')

    def test_learn_page_can_save_a_POST_request(self):
        self.client.post(
            '/sets/QnA/learn',
            data={
                'q_idx': '1',
                'user_text': 'I have question'
            }
        )

        self.assertEqual(PlayerRecord.objects.count(), 1)
        player_record = PlayerRecord.objects.first()
        self.assertEqual(player_record.answer, "I have question")

    def test_learn_page_only_saves_items_when_necessary(self):
        self.client.get('/sets/QnA/learn')
        self.assertEqual(PlayerRecord.objects.count(), 0)

    def test_learn_page_can_show_next_quiz(self):
        response = self.client.post(
            '/sets/QnA/learn',
            data={
                'q_idx': 1,
                'user_text': 'I have question'
            }
        )
        self.assertContains(response, "What is the command?")

    def test_learn_page_can_show_set_description(self):
        response = self.client.post(
            '/sets/QnA/learn',
            data={
                'q_idx': 1,
                'user_text': 'I have question'
            }
        )
        self.assertContains(response, "스택오버플로우에서 활동하려면, 영어로 질문하고 답변할 수 있어야겠죠?")
