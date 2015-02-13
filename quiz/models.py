from django.db import models


class User(models.Model):
    name = models.TextField(default='')
    email = models.EmailField(default='')
    password = models.TextField(default='')

    def __unicode__(self):
        return self.name

class Article(models.Model):
    url = models.TextField(default='')
    title = models.TextField(default='')
    tags = models.TextField(default='')

    def __unicode__(self):
        return self.title

class Sentence(models.Model):
    article = models.ForeignKey(Article, default=None)
    language = models.TextField(default='')
    sentence = models.TextField(default='')
    order = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return self.sentence


class Hint(models.Model):
    sentence = models.ForeignKey(Sentence, default=None)
    hint = models.TextField(default='')
    order = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return self.hint

class QuizResult(models.Model):
    user = models.ForeignKey(User, default=None)
    sentence = models.ForeignKey(Sentence, default=None)
    typed_by_user = models.TextField(default='')
    datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.typed_by_user

######################################

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