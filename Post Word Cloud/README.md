# Reddit post word cloud generator
Script that uses [WordCloud](https://amueller.github.io/word_cloud/index.html) and [PRAW](https://praw.readthedocs.io/en/latest/index.html) to take the comments from a reddit post and generate a word cloud from those comments. 

Note: The only comments used are from the 'first' comments page. Meaning that none of the comments that appear after the 'load more comments' link are used.

## Running the script
* Requires a praw.ini file before using it.

The executing command is in the form of:
```
    ./clouds.py display-option urls
```

display-option: Is an optional argument that has two values you can pass in, dl and plot. 
* dl means download the word clouds without displaying them in a window. These word clouds will be stored in a folder called 'word clouds'.
* plot means display the word clouds in a window without downloading them. 
It is dl by default. 

urls: Can be any number of submission urls. 

Valid urls(urls that go to the comments section) will be downloaded/displayed. Invalid urls will result in an error message, but will not affect any word clouds that have been downloaded/displayed.



