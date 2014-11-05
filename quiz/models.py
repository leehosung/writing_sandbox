from django.db import models

class Phrase(models.Model):
    url = models.TextField(default='')
    english = models.TextField(default='')
    korean = models.TextField(default='')
    category = models.TextField(default='')


class PlayerRecord(models.Model):
    phrase = models.ForeignKey(Phrase)
    answer = models.TextField(default='')
