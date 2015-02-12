from django.contrib import admin
###
from quiz.models import Phrase
from quiz.models import PlayerRecord
from quiz.models import Set
###

from quiz.models import Article
from quiz.models import Sentence    # explicit is better than implicit!
from quiz.models import Hint
from quiz.models import User



######
class PhraseAdmin(admin.ModelAdmin):
    list_display = ['english']


class PlayerRecordAdmin(admin.ModelAdmin):
    pass


class SetAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
#####

class UserAdmin(admin.ModelAdmin):
	list_display = ['name', 'email']

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'url','tags']

class SentenceAdmin(admin.ModelAdmin):
	list_display = ['language', 'sentence']


class HintAdmin(admin.ModelAdmin):
	list_display = ['sentence', 'hint' ]


admin.site.register(Phrase, PhraseAdmin)
admin.site.register(PlayerRecord, PlayerRecordAdmin)
admin.site.register(Set, SetAdmin)
admin.site.register(Article, ArticleAdmin)  # make a link my model and the admin class. 
admin.site.register(Sentence, SentenceAdmin)
admin.site.register(Hint, HintAdmin)
admin.site.register(User, UserAdmin)

