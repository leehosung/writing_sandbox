# coding=utf-8
from django.core.urlresolvers import resolve
from django.test import TestCase

from quiz.views import home_page
from quiz.views import learn_page
from quiz.models import Phrase
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


class PhraseModelTest(TestCase):

    def test_saving_and_retreiving_phrases(self):
        qna_set = Set()
        qna_set.name = "QnA"
        qna_set.save()

        first_phrase = Phrase()
        first_phrase.url = "http://www.stackoverflow.com"
        first_phrase.english = "I have a question"
        first_phrase.korean = "질문이 있어요"
        first_phrase.set = qna_set
        first_phrase.save()

        saved_phrases = Phrase.objects.all()
        self.assertEqual(saved_phrases.count(), 1)

        saved_phrase = saved_phrases[0]

        self.assertEqual(saved_phrase.english, "I have a question")


class PlayerRecordTest(TestCase):

    def test_saving_and_retreiving_player_record(self):
        qna_set = Set()
        qna_set.name = "QnA"
        qna_set.save()

        phrase = Phrase()
        phrase.url = "http://www.stackoverflow.com"
        phrase.english = "I have a question"
        phrase.korean = "질문이 있어요"
        phrase.set = qna_set
        phrase.save()

        player_record = PlayerRecord()
        player_record.phrase = phrase
        player_record.answer = "I have question"
        player_record.save()

        saved_player_records = PlayerRecord.objects.all()
        self.assertEqual(saved_player_records.count(), 1)

        saved_player_record = saved_player_records[0]

        self.assertEqual(saved_player_record.answer, "I have question")


class SetTest(TestCase):

    def test_saving_and_retreiving_set(self):
        set_ = Set()
        set_.name = "QnA"
        set_.description = "스택오버플로우에서 활동"
        set_.save()

        saved_sets = Set.objects.all()
        self.assertEqual(saved_sets.count(), 1)

        saved_set = saved_sets[0]
        self.assertEqual(saved_set.name, "QnA")
        self.assertEqual(saved_set.description, "스택오버플로우에서 활동")
