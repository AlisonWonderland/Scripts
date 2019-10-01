# Reddit image downloader
Script that currently downloads images from the first 10 posts in 'hot' from a subreddit and stores them in a folder called 'images'. It can download images that are directly linked by the post and also download images from imgur albums. It uses PRAW and imgurpython.

To specify the subreddit you want to download images from, insert the name in the empty double quotes in this line of code in the 'main' function:
```python
subreddit = reddit.subreddit("")
```

The number of posts downloaded can be increased without a large effect on the speed of the script since it uses concurrency to do simultaneous downloads/writes to the images.

Note: Used [this article](https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python) to learn about multithreading with request.

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

## What I Learned
* How to download and store images using requests and python file functions.
* Threading, allowing me to speed up the script by doing multiple requests at a time.
* Putting code into a main() function and using 
```python
if __name__ == "__main__":
```
to make the code more readable.
