import os
from django.test import LiveServerTestCase
# from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):

    fixtures = ['quiz/fixtures/test.json']

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
            self.browser = webdriver.Firefox()
            self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

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
        qna_button = self.browser.find_element_by_link_text("QnA")
        qna_button.click()

        # He can see a description for the "QnA" set.
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('스택오버플로우에서 활동하려면, 영어로 질문하고 답변할 수 있어야겠죠?', header_text)

        # He sees a sentence in Korean
        quiz = self.browser.find_element_by_id('text_quiz').text
        self.assertIn("질문이 있어요", quiz)

        # He can see a text box
        inputbox = self.browser.find_element_by_id('input_text_english')
        self.assertEqual(
            inputbox.get_attribute('name'),
            'user_text'
        )

        # He types "I have a question" into a text box
        inputbox.send_keys('I have question')

        # When he hits enter, the pages updates, and now the page shows
        # "I have a question" as a right answer
        inputbox.send_keys(Keys.ENTER)
        answer = self.browser.find_element_by_id('text_correct').text
        self.assertIn("I have a question", answer)

        # He compares it with that he has written
        # He clicks the "Next" button to go on
        next_button = self.browser.find_element_by_id('btn_next')
        next_button.click()

        # He can see another Korean sentence
        quiz = self.browser.find_element_by_id('text_quiz').text
        self.assertIn("명령어가 무엇인가요?", quiz)

        # He types "What is the command?" into a text box
        inputbox = self.browser.find_element_by_id('input_text_english')
        inputbox.send_keys('What is the command?')

        # When he hits enter, the pages updates
        inputbox.send_keys(Keys.ENTER)

        # This is the last question. He can not see the next button
        # He can see the "Go to home" button to select an another set
        home_button = self.browser.find_element_by_link_text('Go to Home')
        home_button.click()

        # User can send a feedback
        send_feedback_button = \
            self.browser.find_element_by_link_text('Send Feedback')
        send_feedback_button.click()
        self.assertIn('Any ideas to improve Writing-Sandbox?',
                      self.browser.title)
        self.browser.back()

        # TODO: remove below line
        return

        # He select the 'Issue' set to learn it
        issue_button = self.browser.find_element_by_link_text("Issue")
        issue_button.click()

        # He sees the sentence in Korean
        quiz = self.browser.find_element_by_id('text_quiz').text
        self.assertIn("사용자는 그들의 소셜 계정으로 로그인 할 수 있습니다.", quiz)

        # He want to quit quiz so click the brand logo
        brand_button = self.browser.\
            find_element_by_link_text('Writing Sandbox')
        brand_button.click()

        # Satisfied, he goes back to sleep
