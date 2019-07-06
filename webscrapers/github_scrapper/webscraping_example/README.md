# Github Scrapper
Basic webscraper that uses selenium to get the titles and languages of a users' most popular repos.

## Example output
Running it on my profile(https://github.com/AlisonWonderland):
![alt text](https://i.imgur.com/VDfpENg.png)

## How to use it
Download the file or copy it.
Currently its set to scrape my popular repos, but you can change that by passing in a new url in browser.get(): 
```python
browser.get('new url')
```
<b>To run:</b>
```
python github_scrapper.py
```
or turn into an excutable:
```
chmod +x github_scrapper.py
```
and run it with:
```
./github_scrapper.py
```
## What I learned/did
* Got introduced to selenium
* Learned how to find and traverse the documentations for selenium. Note: Use this unofficial documentation: https://selenium-python.readthedocs.io/index.html
