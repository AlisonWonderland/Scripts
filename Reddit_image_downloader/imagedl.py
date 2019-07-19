#! /usr/bin/env python

import praw
import requests
import os

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pics")

for submission in subreddit.hot(limit=5):
    if(submission.selftext == ''): #Checking to see if the post has text, if it does ignore it.
        photo_name = submission.title + '.jpg'
        with open(os.path.join('test/',photo_name), 'wb') as f:
            f.write(requests.get(submission.url).content)
    print(submission.url)
