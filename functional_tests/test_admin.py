import os
from django.test import LiveServerTestCase
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

chromedriver = '%s/chromedriver' % os.path.dirname(os.path.abspath(__file__))
if os.path.isfile(chromedriver):
    os.environ['webdriver.chrome.driver'] = chromedriver


class AdminTest(LiveServerTestCase):

    def __init__(self, *args, **kwargs):
        super(AdminTest, self).__init__(*args, **kwargs)
        #if settings.DEBUG == False:
        #    settings.DEBUG = True

    def setUp(self):
        # TODO : DRY
        if 'TRAVIS' in os.environ:
            capabilities = dict()
            capabilities["build"] = os.environ["TRAVIS_BUILD_NUMBER"]
            capabilities["tags"] = [os.environ["TRAVIS_PYTHON_VERSION"], "CI"]
            USERNAME = os.environ.get('SAUCE_USERNAME')
            ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
            sauce_url = "http://%s:%s@localhost:4445"
            self.brower = webdriver.Remote(desired_capabilities=capabilities, command_executor=sauce_url % (USERNAME, ACCESS_KEY))
        else:
            try:
                self.browser = webdriver.Chrome(chromedriver)
            except WebDriverException:
                self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_see_a_list(self):
        # Nasol is the admin of the Writing Sandbox
        # She goes to manage this service
        self.browser.get(self.live_server_url + "/admin")

        # She notices the page title and header mention "page for admin"
        self.assertIn('admin', self.browser.title)

        # She chooses a category to register sentences

        # She types in a pair of English and Korean sentences
        # with its source URL, where she's found them

        # She can order the registered sentences in a different way. Basic principle is that easy ones come first.

        # Satisfied, she goes back to sleep 


if __name__ == '__main__':
    unittest.main()
