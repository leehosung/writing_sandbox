from django.contrib import admin
from quiz.models import Phrase
from quiz.models import PlayerRecord


class PhraseAdmin(admin.ModelAdmin):
    pass


class PlayerRecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phrase, PhraseAdmin)
admin.site.register(PlayerRecord, PlayerRecordAdmin)
