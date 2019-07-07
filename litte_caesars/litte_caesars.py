#! /usr/bin/env python

import time
#For the delay at the end to close the browser after its done
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

def new_profile():
    profiles_file = open('profiles.txt', 'w')
    return 1

def get_profiles():
    #check if file exists
    try:
        profiles_file = open('profiles.txt')
    except:
        while(1):
            response = input("profiles.txt doesn't exist. Would you like to create it?\nEnter 'y' to create or 'n' to go back to menu.\n")
            if(response == 'y'):
                return new_profile()
            elif(response == 'n'):
                return
            else:
                print('Invalid. Try again.')

    profiles = profiles_file.readlines()
    #Print number of profile along side the actual email and password
    for number, profile in enumerate(profiles):
        print(number, profile)
    

    #Choose profile/login


    profiles_file.close()

def intro():
    print("Enter 'done' when you're ready to proceed to your order")
    print("Enter '1' to show all usernames and choose one. 2 to enter a new login.")

    while(1):
        user_input = input() #or use raw input for string
        if(user_input == '1'):
            get_profiles()
        elif(user_input == '2'):
            new_profile()
        else:
            print('Invalid input')


intro()

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path='/mnt/d/Users/dimitri/Desktop/chromedriver.exe', chrome_options=option)

# Go to little caesars website
browser.get("https://littlecaesars.com/en-us/")

# Wait 20 seconds for page to load
timeout = 20
try:
    # Wait until the login logo shows up.
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='sc-dqBHgY AYCxi']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# Press the button
login_button = browser.find_element_by_xpath("//a[@class='sc-dqBHgY AYCxi']")
print(type(login_button))
login_button.click()

# #Print titles
# print("\nTITLES:")
# print(titles, '\n')

# # Get the languages
# languages = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
# languages = [language.text for language in languages]

# #Print Languages
# print("LANGUAGES:")
# print(languages, '\n')


# for title, language in zip(titles, languages):
#     print("RepoName : Language")
#     print(title + ": " + language, '\n')

# time.sleep(5);
# browser.close();
