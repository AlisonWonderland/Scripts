#! /usr/bin/env python

import praw
import requests
import os

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pics")

for submission in subreddit.hot(limit=5):
    #change .jpg ending for non .jpg
    photo_path = 'test/' + submission.title + '.jpg'

    #Checking to see if the post has no text and if it was not downloaded, ignore it otherwise.
    if(submission.selftext == '' and (not os.path.exists(photo_path))): 
        with open(photo_path, 'wb') as f:
            f.write(requests.get(submission.url).content)

"""
Expansion ideas:
Combine with flask to create gallery from links
Add folders based on name/facial recognition
"""