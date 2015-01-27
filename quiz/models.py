from django.db import models


class Article(models.Model):
    url = models.TextField(default='')
    title = models.TextField(default='')
    tags = models.TextField(default='')


class Sentence(models.Model):
    article = models.ForeignKey(Article, default=None)
    language = models.TextField(default='')
    sentence = models.TextField(default='')
    order = models.PositiveSmallIntegerField(default=0)


class Set(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Phrase(models.Model):
    title = models.TextField(default='')
    url = models.TextField(default='')
    english = models.TextField(default='')
    korean = models.TextField(default='')
    set = models.ForeignKey(Set)
    difficulty = models.PositiveSmallIntegerField(default=32767)


class PlayerRecord(models.Model):
    phrase = models.ForeignKey(Phrase)
    answer = models.TextField(default='')
