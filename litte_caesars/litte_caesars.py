#! /usr/bin/env python

import time, sys
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

def choose_profile(profiles):
    print("Enter number of profile you want to use or 'q' to return to menu: ", end = "")        

    while (1):
        user_input = input()

        #Check if input is number or string
        if(user_input.isdigit()):
            user_input = int(user_input)
        elif(user_input == 'q'):
            print() #For clearer output
            return None
        #If else is entered, it means user inputted an invalid string
        else:
            print('Invalid. Try again: ', end = "")
            continue

        #Reaching this point means that user input is an int and it needs to be
        #be a valid index of the list 'profiles'
        if((user_input < 0) or (user_input > len(profiles) - 1)):
            print('Invalid. Try again: ', end = "")
        else:
            return profiles[user_input]

def new_profile():
    profiles_file = open('profiles.txt', 'a+')
    
    #Asking for login info
    while(1):
        print('\nEnter your login email: ', end = "")
        email = input()

        print('Enter your login password: ', end = "")
        password = input()

        print('\nYour username:', email, '| Your password:', password)
        print("Is this correct? Enter y to proceed, q to return to menu, anything else to repeat: ", end = "")
        response = input()
        print() #For whitespace

        if(response == 'y'):
            profiles_file.write(email + ' ' + password + '\r\n') #Add login to file
            break
        elif(response == 'q'):
            break

    profiles_file.close()
    return 

def get_profiles():
    #check if file exists
    try:
        profiles_file = open('profiles.txt')
    except:
        while(1):
            response = input("profiles.txt doesn't exist. Would you like to create it?\nEnter 'y' to create or 'n' to go back to menu.\n")
            if(response == 'y'):
                return 
            elif(response == 'n'):
                return
            else:
                print('Invalid. Try again.')

    profiles = profiles_file.readlines() # Store logins in a list

    #Check if there are profiles in the file
    if(not len(profiles)):
        print('\nNo logins stored. Add new ones.\n')

    #Print number of the login alongside the actual email and password
    else:
        print('\n-------------------------------------------------------------------')
        for number, profile in enumerate(profiles):
            print(number, profile)
        print('-------------------------------------------------------------------\n')

    profiles_file.close()

    return profiles

def intro():
    while(1):
        print("Enter '1' to show all usernames and choose one. '2' to enter a new login.\nEnter q if you want to exit.\n")
        user_input = input()
        if(user_input == '1'):
            #Print available profiles
            profiles = get_profiles()
            #If profiles is empty then repeat menu msg
            if(len(profiles)):
                profile = choose_profile(profiles)
                if(profile == None):
                    continue
                else:
                    return profile
        elif(user_input == '2'):
            new_profile()
        elif(user_input == 'q'):
            print('Exiting program.')
            sys.exit()
        else:
            print('Invalid input')

#Get login
login_info = intro()
login_info = login_info.split(' ')

#Little caesars username
lc_email = login_info[0]

#Little caesars password, remove the newline before storing it into lc_password
newline_index = login_info[1].find("\n")
lc_password = login_info[1][0:newline_index]

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

browser = webdriver.Chrome(executable_path='/mnt/d/Users/dimitri/Desktop/chromedriver.exe', chrome_options=option)

# Go to little caesars website
browser.get("https://littlecaesars.com/en-us/")

# Wait 20 seconds for page to load, to press login button
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

# Wait 20 seconds before entering login info
timeout = 20
try:
    # Wait until the login logo shows up.
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='sc-hZeNU hRsEcQ']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

email_input = browser.find_element_by_xpath("//input[@id='B1xobMEeZr']")
email_input.send_keys(lc_email)

password_input = browser.find_element_by_xpath("//input[@id='H1-oWG4lZH']")
password_input.send_keys(lc_password)

