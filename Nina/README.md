# Nina 
A script that uses [IBM's Personality Insights API](https://www.ibm.com/watson/services/personality-insights/)and [PRAW](https://praw.readthedocs.io/en/latest/index.html) to print insight into a Reddit users personality. The results shouldn't be taken as cold hard facts, but its interesting to see the insights the AI gives.

Currently it uses 45 of the newest comments.

## Running the script
* Requires a praw.ini file before using it.

The executing command is in the form of:
```
    ./nina.py username1 username2....
```

Note: usernames are the only arguments. They must be separated by spaces. An unlimited amount of users can be used, but the more you use the slower it gets.