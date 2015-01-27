# coding=utf-8
from django.test import TestCase

from quiz.models import Article
from quiz.models import Sentence
from quiz.models import Phrase
from quiz.models import PlayerRecord
from quiz.models import Set

"""
user : id, name, email, password,
quiz_result : id, user_id, sentence_id, attempt
article : id, url, title, tags
sentence : id, article_id, language, sentence, order
hint : id, sentence_id, hint, order
"""


class SentenceModelTest(TestCase):

    def test_saving_and_retreiving_phrases(self):
        article = Article()
        article.url = "http://d0.awsstatic.com/whitepapers/AWS_DevOps.pdf"
        article.title = "Introduction to DevOps on AWS"
        article.tags = "AWS, DevOps"
        article.save()

        # save
        sentence = Sentence()
        sentence.article = article
        sentence.language = "English"
        sentence.sentence = "As innovation accelerates and customer needs "
        "rapidly evolve, businesses must become increasingly agile."
        sentence.order = 0
        sentence.save()

        saved_sentences = Sentence.objects.all()
        self.assertEqual(saved_sentences.count(), 1)

        saved_sentence = saved_sentences[0]

        self.assertEqual(saved_sentence.language, "English")


class ArticleModelTest(TestCase):

    def test_saving_and_retreiving_phrases(self):
        # save
        article = Article()
        article.url = "http://d0.awsstatic.com/whitepapers/AWS_DevOps.pdf"
        article.title = "Introduction to DevOps on AWS"
        article.tags = "AWS, DevOps"
        article.save()

        # Getting
        saved_articles = Article.objects.all()
        self.assertEqual(saved_articles.count(), 1)

        saved_article = saved_articles[0]

        self.assertEqual(saved_article.title, "Introduction to DevOps on AWS")


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
