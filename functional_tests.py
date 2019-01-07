from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://10.100.8.236:8000')

assert 'Django' in browser.title