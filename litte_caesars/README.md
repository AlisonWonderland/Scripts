# Little Caesers ordering script, a failed project
This a 'failed' attempt at making a script that can complete a Little Caesars order. I say failed because its impossible to use selenium to input your login email and password. This is because Little Caesars constantly updates the ids and class values of the html elements. And you need the ids and class values to be static otherwise selenium can't target them. Plus, there is a captcha button that needs to be pressed. Still, it was a good learning experience.

It was supposed to open a new browser, log you in, order for you(you would have to specify the order beforehand), select the order time and finally pay. 

Only got up to the log in phase.

## What I learned
* File input/output in python.
* enumerate(). Which is a built-in function that creates an iterator alongside a list, so that you can number items in the list.
* appending to a file using open(file_name, "a+"). This will create a new file if it doesn't exist and allow us to add to a file.
* Little Caesars takes their security against bots and scripts seriously.
