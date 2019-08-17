#! /usr/bin/env python
import praw
import numpy as np
import pandas as pd
import sys
import os
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt



postTitles = []

def generateWordClouds(urlList):
    reddit = praw.Reddit('bot1')
    clouds = []

    for url in urlList:
        try:
            post = reddit.submission(url=url)
            post.comments.replace_more(limit=None) # Means that 'load more comments' is never used
            postComments = "\n".join(comment.body for comment in post.comments.list())
            clouds.append(WordCloud( width=1300, height=700).generate(postComments))
            postTitles.append(post.title)
        except praw.exceptions.ClientException as e:
            print(e)

    if len(clouds) == 0:
        sys.exit("ERROR: NO VALID URL(S) GIVEN.")

    return clouds

def createPlot(clouds):
    for i in range(len(clouds)):
        figure = plt.figure(postTitles[i], figsize=(10,8)) 
        plt.imshow(clouds[i], interpolation='bilinear')
        plt.axis("off")
        
    plt.show()

def downloadWordClouds(clouds):
   for i in range(len(clouds)):
        figure = plt.figure(figsize=(20,10)) 
        plt.imshow(clouds[i], interpolation='bilinear')
        plt.axis("off")

        try:
            os.makedirs('word clouds/')
        except FileExistsError:
            # directory already exists
            pass
        figure.savefig('word clouds/' + postTitles[i] + '.png') 



def main(argv):
    if len(argv) == 0:
        sys.exit("ERROR: NO ARGUMENT(S) GIVEN")
    
    if argv[0] == 'dl':
        clouds = generateWordClouds(argv[1:])
        downloadWordClouds(clouds)
    
    elif argv[0] == 'plot':
        clouds = generateWordClouds(argv[1:])
        createPlot(clouds)

    # Downloading the word cloud image is the default option
    else:
        clouds = generateWordClouds(argv[1:])
        downloadWordClouds(clouds)

if __name__ == "__main__":
   main(sys.argv[1:])