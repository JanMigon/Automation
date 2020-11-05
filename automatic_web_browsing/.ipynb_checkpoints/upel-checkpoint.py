# -*- coding: utf-8 -*-
import time
import selenium

from configuration.config import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get(config['url'])
cookies = browser.find_element_by_name('accept-cookies')
cookies.send_keys(Keys.ENTER)

username_field = browser.find_element_by_id('username')
password_field = browser.find_element_by_id('password')

username_field.clear()
username_field.send_keys(config['username'])

password_field.clear()
password_field.send_keys(config['password'])
password_field.send_keys(Keys.ENTER)

course_field = browser.find_element_by_link_text(config['course'])
course_field.send_keys(Keys.ENTER)

activity_instance = browser.find_element_by_xpath(config['link_of_interest'])
activity_instance.send_keys(Keys.ENTER)

try:
    activity_registration = browser.find_element_by_link_text('Zarejestruj obecność')
    activity_registration.send_keys(Keys.ENTER)
except selenium.common.exceptions.NoSuchElementException:
    print('Element not found')


time.sleep(3)
browser.quit()
