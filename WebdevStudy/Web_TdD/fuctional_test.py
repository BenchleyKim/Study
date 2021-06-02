from selenium import webdriver


browser = webdriver.Chrome(executable_path="C:/Users/bottlechrome/Documents/GitHub/DeepDive/crawling/chromedriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title