#! /usr/bin/env python
import praw
import prawcore
import sys
import path
import os
import json
from ibm_watson import PersonalityInsightsV3


personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    iam_apikey='HlLLaRow1_RtikoMNWCt0G5PN5nHk60xhOcxYD0sQV67',
    url='https://gateway.watsonplatform.net/personality-insights/api'
)

def getUserComments(usernames):
    userCommentsList = []
    validUsers = []
    reddit = praw.Reddit('bot1')

    # Usernames may be typed/copied incorrectly
    for i in range(len(usernames)):
        try:
            user = reddit.redditor(usernames[i])
            userComments = " ".join(comment.body for comment in user.comments.new(limit=50))
            userCommentsList.append(userComments)
            validUsers.append(usernames[i])
        except prawcore.exceptions.NotFound as e:
            print(e)

    if len(userCommentsList) == 0:
        sys.exit("No valid usernames given")

    return [userCommentsList, validUsers]


def main(usernames):
    if len(usernames) == 0:
        sys.exit("No usernames provided")

    data = getUserComments(usernames)
    userComments = data[0]
    validUsers = data[1]
     # Last thing worry about limit

    profiles = []
    
    for i in range(len(userComments)):
        profiles.append(personality_insights.profile(
            userComments[i],
            'application/json'
        ).get_result())
    
    for i in range(len(profiles)):
        print()


if __name__ == "__main__":
   main(sys.argv[1:])
