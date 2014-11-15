import os
from django.test import LiveServerTestCase
# from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

chromedriver = '%s/chromedriver' % os.path.dirname(os.path.abspath(__file__))
if os.path.isfile(chromedriver):
    os.environ['webdriver.chrome.driver'] = chromedriver


class NewVisitorTest(LiveServerTestCase):

    fixtures = ['quiz/fixtures/functional_test.json']

    def __init__(self, *args, **kwargs):
        super(NewVisitorTest, self).__init__(*args, **kwargs)
        # if settings.DEBUG == False:
        #    settings.DEBUG = True

    def setUp(self):
        if 'SAUCE' in os.environ:
            capabilities = {'platform': 'Mac OS X 10.9',
                            'browserName': 'chrome',
                            'version': '31', 'name': self.id()}
            capabilities["build"] = os.environ["TRAVIS_BUILD_NUMBER"]
            capabilities["tags"] = [os.environ["TRAVIS_PYTHON_VERSION"], "CI"]
            USERNAME = os.environ.get('SAUCE_USERNAME')
            ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
            sauce_url = "http://%s:%s@localhost:4445/wd/hub"
            self.browser = webdriver.Remote(
                desired_capabilities=capabilities,
                command_executor=sauce_url % (USERNAME, ACCESS_KEY))
            self.browser.implicitly_wait(30)
        else:
            try:
                self.browser = webdriver.Chrome(chromedriver)
            except WebDriverException:
                self.browser = webdriver.Firefox()
            self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_see_a_quiz(self):
        if 'SAUCE' in os.environ:
            server_url = os.environ["SAUCE_SERVER_URL"]
        else:
            server_url = self.live_server_url
        # Hosung has heard about a cool new online writing training app.
        # He goes to check out its homepage
        self.browser.get(server_url)

        # He notices the page title and header mention "Writing Sandbox"
        self.assertIn('Writing Sandbox', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Home', header_text)

        # He logs into the service.

        # He chooses the QnA set to practice
        self.check_for_row_in_list_table('1: QnA')
        qna_button = self.browser.find_element_by_css_selector(
            "tr:nth-child(1) > td:nth-child(1) > p > a")
        qna_button.click()

        # He sees a sentence in Korean
        quiz = self.browser.find_element_by_id('id_text_quiz').text
        self.assertIn("질문이 있어요", quiz)

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
        answer = self.browser.find_element_by_id('id_confirm_answer').text
        self.assertIn("I have a question", answer)

        # He compares it with that he has written
        # He clicks the "Next" button to go on
        next_button = self.browser.find_element_by_id('id_btn_next')
        next_button.click()

        # He can see another Korean sentence
        quiz = self.browser.find_element_by_id('id_text_quiz').text
        self.assertIn("명령어가 무엇인가요?", quiz)

        # This is a last quiestion. He can not see the next button
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_id('id_btn_next')

        # Satisfied, he goes back to sleep
