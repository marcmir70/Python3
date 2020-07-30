# Practice Python, Exercise 17 - from 20140606 done (from solution but differently) in 20190729
# - ref: https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# Exercise: Use BeautifulSoup and requests Python packages to print out a
#           list of all article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all("h2"):
# for story_heading in soup.find_all("h2", "</h2>"):
## MarcMir70 - The code below has errors (today for the 4th line)
##    if story_heading.a:
##        print('1. '+story_heading.a.text.replace("\n", " ").strip())
##    else:
##        print('2. '+story_heading.contents[0])

### MarcMir70 - The code below shows the entire HTML clauses for each article text!
    if story_heading.a:
        print(story_heading.a)
    else:
        print(story_heading)