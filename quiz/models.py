from django.db import models


class Set(models.Model):
    name = models.TextField(default='')

    def __str__(self):
        return self.name


class Phrase(models.Model):
    url = models.TextField(default='')
    english = models.TextField(default='')
    korean = models.TextField(default='')
    set = models.ForeignKey(Set)


class PlayerRecord(models.Model):
    phrase = models.ForeignKey(Phrase)
    answer = models.TextField(default='')
