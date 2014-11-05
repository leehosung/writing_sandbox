from selenium import webdriver
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

        # He notices the page title and header mention "writing sandbox"
        self.assertIn('Writing Sandbox', self.browser.title)
        self.fail('Finish the test!')

        # He logs into the service. 

        # He chooses a category to practice

        # He sees a sentence in Korean

        # He writes a sentence in English 

        # He types enters, and a sentence which Admin has registered in advance will show up

        # He compares it with that he has written

        # He goes on

        # Satisfied, he goes back to sleep 

if __name__ == '__main__':
    unittest.main()
