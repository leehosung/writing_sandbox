from selenium import webdriver

browser = webdriver.Firefox()

# Hosung has heard about a cool new online writing training app.
# He goes to check out its homepage
browser.get('http://localhost:8000')

# He notices the page title and header mention "writing sandbox"
assert 'writing sandbox' in browser.title

# He logs into the service. 

# He chooses a category to practice

# He sees a sentence in Korean

# He writes a sentence in English 

# He types enters, and a sentence which Admin has registered in advance will show up

# He compares it with that he has written

# He goes on

# Satisfied, he goes back to sleep 
browser.quit()
