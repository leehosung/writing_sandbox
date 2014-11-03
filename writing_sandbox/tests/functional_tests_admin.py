from selenium import webdriver

browser = webdriver.Firefox()

# Nasol is the admin of the Writing Sandbox
# She goes to manage this service
browser.get('http://localhost:8000/admin')

# She notices the page title and header mention "writing sandbox"
assert 'writing sandbox' in browser.title

# She chooses a category to register sentences

# She types in a pair of English and Korean sentences
# with its source URL, where she's found them

# She can order the registered sentences in a different way. Basic principle is that easy ones come first.

# Satisfied, she goes back to sleep 
browser.quit()
