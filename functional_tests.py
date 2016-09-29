from selenium import webdriver

browser = webdriver.Chrome('/home/rayyu/chrome/chromedriver')

browser.get('http://localhost:8000')

assert 'Django' in browser.title
