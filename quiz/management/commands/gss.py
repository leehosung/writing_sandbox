# from optparse import make_option
from django.core.management.base import BaseCommand
from django.conf import settings
# from django.core.management.base import CommandError
import gspread
# from oauth2client.client import SignedJwtAssertionCredentials
from quiz.models import Phrase
from quiz.models import Set


class Command(BaseCommand):
    help = 'Getting phrases from Google Spread Sheets'

    # option_list = BaseCommand.option_list + (
    #     make_option(
    #         '--authorize',
    #         action='store_true',
    #         dest='authorize',
    #         default=False,
    #         help='Authorization using OAuth2',
    #     ),
    # )

    def handle(self, *args, **options):
        # SIGNED_KEY = open(settings.GOOGLE_SIGNED_KEY, 'rb').read()
        # scope = [
        #    'https://spreadsheets.google.com/feeds',
        #    'https://docs.google.com/feeds']
        # credentials = SignedJwtAssertionCredentials(
        #    settings.GOOGLE_SERVICE_ACCOUNT,
        #    SIGNED_KEY, scope)
        # gc = gspread.authorize(credentials)
        # Login with your Google account
        gc = gspread.login(settings.GOOGLE_ID, settings.GOOGLE_PW)

        # Open a worksheet from spreadsheet with one shot
        # wks = gc.open("SANDBOX - Admin").sheet1
        wks = gc.open_by_key(settings.WRITING_SAND_BOX_ADMIN_KEY).sheet1

        # Fetch a cell range
        rows = wks.get_all_values()
        row_count = 0
        for row in rows[1:]:
            (set_name, title, url, korean, english,
                sentence_length, difficulty) = row
            if title == '':
                continue
            row_count += 1
            try:
                set_ = Set.objects.get(name=set_name)
            except Set.DoesNotExist:
                set_ = Set.objects.create(name=set_name)
                self.stdout.write("NEW SET :", set_name)

            phrases = Phrase.objects.filter(korean=korean)
            if len(phrases) > 0:
                # TODO - update phrase
                continue
            phrase = Phrase.objects.create(
                url=url, english=english, korean=korean,
                set=set_, difficulty=difficulty)
            self.stdout.write("NEW :", phrase.english)
        self.stdout.write("%d rows are proccesed." % row_count)
        # raise CommandError('Error')
