import os
from django.test import LiveServerTestCase
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

chromedriver = '%s/chromedriver' % os.path.dirname(os.path.abspath(__file__))
if os.path.isfile(chromedriver):
    os.environ['webdriver.chrome.driver'] = chromedriver


class NewVisitorTest(LiveServerTestCase):

    def __init__(self, *args, **kwargs):
        super(NewVisitorTest, self).__init__(*args, **kwargs)
        #if settings.DEBUG == False:
        #    settings.DEBUG = True

    def setUp(self):
        if 'TRAVIS' in os.environ:
            capabilities = {'platform': 'Mac OS X 10.9', 'browserName': 'chrome', 'version': '31', 'name': self.id()}
            capabilities["build"] = os.environ["TRAVIS_BUILD_NUMBER"]
            capabilities["tags"] = [os.environ["TRAVIS_PYTHON_VERSION"], "CI"]
            USERNAME = os.environ.get('SAUCE_USERNAME')
            ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
            sauce_url = "http://%s:%s@localhost:4445/wd/hub"
            self.browser = webdriver.Remote(desired_capabilities=capabilities, command_executor=sauce_url % (USERNAME, ACCESS_KEY))
            self.browser.implicitly_wait(30)
        else:
            try:
                self.browser = webdriver.Chrome(chromedriver)
            except WebDriverException:
                self.browser = webdriver.Firefox()
            self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_see_a_quiz(self):
        # Hosung has heard about a cool new online writing training app.
        # He goes to check out its homepage
        if 'TRAVIS' in os.environ:
            self.browser.get('http://writing-sandbox.herokuapp.com')
        else:
            self.browser.get(self.live_server_url)

        # He notices the page title and header mention "Writing Sandbox"
        self.assertIn('Writing Sandbox', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Quiz', header_text)

        # He logs into the service. 

        # He chooses a category to practice

        # He sees a sentence in Korean

        # He can see a text box
        inputbox = self.browser.find_element_by_id('id_input_english')
        self.assertEqual(
                inputbox.get_attribute('name'),
                'user_text'
        )

        # He types "I have a question" into a text box
        inputbox.send_keys('I have question')

        # When he hits enter, the pages updates, and now the page shows
        # "I have a question" as a right answer
        inputbox.send_keys(Keys.ENTER)

        # He types enters, and a sentence which Admin has registered in advance will show up

        # He compares it with that he has written

        # He goes on

        # Satisfied, he goes back to sleep 
