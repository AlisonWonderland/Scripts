#! /usr/bin/env python

from imgurpython import ImgurClient
from datetime import datetime
from bs4 import BeautifulSoup
import praw
import requests
import os
import re

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

# The album/gallery id would be WDe1xRO when the link is https://imgur.com/gallery/WDe1xRO
def get_album_id(album_url):
    for i in range(len(album_url)):
        if(album_url[i] == '/'):
            id_start_index = i + 1 #Add one so we don't include the second '/' from /gallery/ or /a/
    
    album_id = album_url[id_start_index:len(album_url)]
    return album_id

#The image id would be Cai5Ore, when the url is https://i.imgur.com/Cai5Ore.jpg
def get_image_id(image_url):
    for i in range(len(image_url)):
        if(image_url[i] == '/'):
            id_start_index = i + 1 
    
    for i in range(id_start_index, len(image_url)):
        if(image_url[i] == '.'):
            id_end_index = i
            break
    
    image_id = image_url[id_start_index:id_end_index]
    return image_id

def album_download(client, album_id):
    images = client.get_album_images(album_id)
    for image in images:
        image_download(image.link)

def image_download(image_url, title=None):
    if(title == None):
        title = get_image_id(image_url)

    photo_path = 'test/' + title + get_extension(image_url)

    #This will download an image only when an image doesn't have the same title as a downloaded one
    if(not os.path.exists(photo_path)): 
        with open(photo_path, 'wb') as f:
            f.write(requests.get(image_url).content)

imgur_client_id = '' 
imgur_client_secret = ''

client = ImgurClient(imgur_client_id, imgur_client_secret)

start = datetime.utcnow()

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("") 

for submission in subreddit.hot(limit=5):
    if(is_valid_image(submission.url)):
       image_download(submission.url, submission.title);

    elif(is_imgur_album(submission.url)):
        album_id = get_album_id(submission.url)
        album_download(client, album_id)

elasped = datetime.utcnow() - start
print(elasped)
