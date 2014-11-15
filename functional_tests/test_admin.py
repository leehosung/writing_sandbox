from django.test import LiveServerTestCase


class AdminTest(LiveServerTestCase):

    def __init__(self, *args, **kwargs):
        super(AdminTest, self).__init__(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_can_see_a_list(self):
        pass
        # Nasol is the admin of the Writing Sandbox
        # She goes to manage this service

        # She notices the page title and header mention "page for admin"

        # She chooses a category to register sentences

        # She types in a pair of English and Korean sentences
        # with its source URL, where she's found them

        # She can order the registered sentences in a different way.
        # Basic principle is that easy ones come first.

        # Satisfied, she goes back to sleep
