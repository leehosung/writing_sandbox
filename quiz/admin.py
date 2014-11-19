from django.contrib import admin
from quiz.models import Phrase
from quiz.models import PlayerRecord
from quiz.models import Set


class PhraseAdmin(admin.ModelAdmin):
    list_display = ['english']


class PlayerRecordAdmin(admin.ModelAdmin):
    pass


class SetAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


admin.site.register(Phrase, PhraseAdmin)
admin.site.register(PlayerRecord, PlayerRecordAdmin)
admin.site.register(Set, SetAdmin)
