#This module will pull all links from the html code from https://www.census.gov/programs-surveys/popest.html

import bs4
import requests
from bs4 import BeautifulSoup

#Enter the URL and assign to 'url' variable
url = ('http://www.census.gov/programs-surveys/popest.html')
page = requests.get(url)

#Creating the soup
soup = BeautifulSoup(page.text, "html.parser")

#This will get the links from the website.
siteLinks = soup.find_all('a', href=True)

#Sets string to search to determine relative links
linkPrefix = '/'

#String to propend to relative URLs to make absolute URIs
baseURL = 'https://www.census.gov'

#Creates an array for the stripped links
cleanLinks = []

#This strips everything out but the actual links
for a in siteLinks:
    cleanLinks.append (a['href'])
    
#creates array for next step
completeLinks = []

#creates substring to exclude
substring = '#'

#Adds appropriate prefix to all relative links
for i in cleanLinks:
    if i.startswith(linkPrefix):
        g = baseURL + i
        completeLinks.append (g)
    else:
        if substring in i:
            continue
        else:
            completeLinks.append (i)

#Will remove all duplicates from link list.
finalLinks = list(dict.fromkeys(completeLinks))

#Writes values to file
with open('/Users/Scot/OneDrive - University of Florida/School/WGU/Fall2020/C996 - Programming in Python/listitems.csv','w') as f:
	for item in finalLinks:
		f.write(item + ",")
