# Reddit image downloader
Script that currently downloads images from the first 5 posts in 'hot' from a subreddit and stores them in a folder called 'test'. It can download images that are directly linked by the post and also download images from imgur albums. It uses PRAW, a Reddit API wrapper, and imgurpython, a python client for the Imgur api, to download Imgur albums. 

To specify the subreddit you wan to download images from, insert the name in the empty double quotes in this line of code in the 'main' function:
```python
subreddit = reddit.subreddit("")
```

Note: You may not be able to view gifv and mpv files depending on your OS and media players.
Note: Imgurpython is no longer supported. I plan on changing the script to adapt to the new api.

## Instructions to run script
Since this script requires it to be registered through a Reddit and Imgur, you have to have an account for both websites and register the script at:
```
https://api.imgur.com/oauth2/addclient
https://www.reddit.com/prefs/apps/
```

Install praw and imgurpython:
```
pip install imgurpython
pip install --upgrade praw
```

Create a praw.ini file, use this:
https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html

Include the praw.ini file in the same directory as your script file.

## Things to improve
* The code could run faster using threads, so that's the next feature to implement.

## What I Learned
* How to download and store images using requests and python file functions.
* Threading can speed up the script by doing multiple requests at a time.
* Putting code into a main() function and using 
```python
if __name__ == "__main__":
```
to make the code more readable.