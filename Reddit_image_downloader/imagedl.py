#! /usr/bin/env python

from datetime import datetime
from bs4 import BeautifulSoup
import praw
import requests
import os
import re
import sys #for sys.exit(). remove after testing functions


def is_valid_image(image_url):
    #check if link is an image by looking at file extension
    valid_extensions = ['jpg', 'jpeg', 'mpv', 'gifv', 'gif']
    for i in range(len(valid_extensions)):
        if(image_url[len(image_url) - 3:len(image_url)] == valid_extensions[i] or image_url[len(image_url) - 4:len(image_url)] == valid_extensions[i]):
            return True
    return False

def is_imgur_album(album_url):
    if (re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", album_url) != None):
        return True
    return False

def get_extension(image_url):
    extensions = ['jpg', 'jpeg', 'mpv', 'gifv', 'gif']
    for i in range(len(extensions)):
        if(image_url[len(image_url) - 3:len(image_url)] == extensions[i] or image_url[len(image_url) - 4:len(image_url)] == extensions[i]):
            return '.' + extensions[i]

def album_download(album_page):
    album_soup = BeautifulSoup(album_page.content, 'html.parser')
    for image in album_soup.findAll('img'):
        print(image.get('src'))

start = datetime.utcnow()

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("lizwenya")

for submission in subreddit.hot(limit=5):
    if(is_valid_image(submission.url)):
        photo_path = 'test/' + submission.title + get_extension(submission.url)

        #This will download an image only when an image doesn't have the same title as a downloaded one
        if(not os.path.exists(photo_path)): 
            with open(photo_path, 'wb') as f:
                f.write(requests.get(submission.url).content)

    elif(is_imgur_album(submission.url)):
        album_page = requests.get(submission.url)
        album_download(album_page)

elasped = datetime.utcnow() - start
print(elasped)

"""
Expansion ideas:
Combine with flask to create gallery from links
Add folders based on name/facial recognition
"""