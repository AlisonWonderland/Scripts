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
    iam_apikey='',
    url='https://gateway.watsonplatform.net/personality-insights/api'
)


def traits(persona, user):
    personality = persona["personality"]
    needs = persona["needs"]

    print("From the BIG 5 traits they have:\n")

    for i in range(len(personality)):
        big5TraitName = personality[i]["name"]
        childTraits = personality[i]["children"]

        if personality[i]["percentile"] > 0.7:
            print("They have Big 5 trait " + big5TraitName + ", based on their comments") 
        
        else:
            print("They haven't shown Big 5 trait " + big5TraitName + ", maybe not enough data. Or they truly don't have it.")

        for j in range(len(childTraits)):
            if childTraits[j]["percentile"] > 0.7:
                print("Under " + big5TraitName + " they've shown " + childTraits[j]["name"])
        
        print("It likes like they need:")
        if len(needs) == 0:
            print("Nothing it seems")
        else:
            for k in range(len(needs)):
                print(needs[k]["name"])
        print("\n")

    return


def getUserComments(usernames):
    userCommentsList = []
    validUsers = []
    reddit = praw.Reddit('bot1')

    # Usernames may be typed/copied incorrectly
    for i in range(len(usernames)):
        try:
            user = reddit.redditor(usernames[i])
            userComments = " ".join(comment.body for comment in user.comments.new(limit=45))
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

    profiles = []
    
    for i in range(len(userComments)):
        profiles.append(personality_insights.profile(
            userComments[i],
            'application/json'
        ).get_result())
    
    for i in range(len(profiles)):
        print("\n-----------------" + validUsers[i] + " Personality Insights-----------------")
        traits(profiles[i], validUsers[i])
    
    return

if __name__ == "__main__":
   main(sys.argv[1:])
