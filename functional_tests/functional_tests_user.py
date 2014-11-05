from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class UserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_a_quiz(self):
        # Hosung has heard about a cool new online writing training app.
        # He goes to check out its homepage
        self.browser.get('http://localhost:5000')

        # He notices the page title and header mention "Writing Sandbox"
        self.assertIn('Writing Sandbox', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Quiz', header_text)

        # He logs into the service. 

        # He chooses a category to practice

        # He sees a sentence in Korean

        # He can see a text box
        inputbox = self.browser.find_element_by_id('id_input_english')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Write an English sentense'
        )

        # He types "I have a question" into a text box
        inputbox.send_keys('I have question')

        # When he hits enter, the pages updates, and now the page shows
        # "I have a question" as a right answer
        inputbox.send_keys(Keys.ENTER)
        self.fail('Finish the test!')

        # He types enters, and a sentence which Admin has registered in advance will show up

        # He compares it with that he has written

        # He goes on

        # Satisfied, he goes back to sleep 

if __name__ == '__main__':
    unittest.main()
