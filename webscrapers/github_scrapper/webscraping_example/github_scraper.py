#! /usr/bin/env python

import time

from selenium import webdriver 
#To launch browser
from selenium.webdriver.common.by import By 
#Helps us find things on a page. Like a login
from selenium.webdriver.support.ui import WebDriverWait 
#To wait for the page to load.
from selenium.webdriver.support import expected_conditions as EC 
#Makes sure that page has loaded by looking at the the thing we specify to look at.
from selenium.common.exceptions import TimeoutException
#For handling timeouts

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path='/mnt/d/Users/dimitri/Desktop/chromedriver.exe', chrome_options=option)

# Go to desired website
browser.get("https://github.com/AlisonWonderland")

# Wait 20 seconds for page to load
timeout = 20
try:
    # Wait until the final element [Avatar link] is loaded.
    # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
    # the last things to be loaded.
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full height-full avatar-before-user-status']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# Get the titles
titles = browser.find_elements_by_xpath("//a[@class='text-bold flex-auto']")
titles = [title.text for title in titles]

#Print titles
print("TITLES:")
print(titles, '\n')

# Get the languages
languages = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
languages = [language.text for language in languages]

#Print Languages
print("LANGUAGES:")
print(languages, '\n')


for title, language in zip(titles, languages):
    print("RepoName : Language")
    print(title + ": " + language, '\n')

time.sleep(2);
browser.close();
