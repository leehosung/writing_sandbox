from selenium import webdriver
import unittest


class AdminTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quite()

    def test_can_see_a_list(self):
        # Nasol is the admin of the Writing Sandbox
        # She goes to manage this service
        self.browser.get('http://localhost:8000/admin')

        # She notices the page title and header mention "writing sandbox"
        self.assertIn('writing sandbox', self.browser.title)
        self.fail('Finish the test!')

        # She chooses a category to register sentences

        # She types in a pair of English and Korean sentences
        # with its source URL, where she's found them

        # She can order the registered sentences in a different way. Basic principle is that easy ones come first.

        # Satisfied, she goes back to sleep 

if __name__ == '__main__':
    unittest.main()
