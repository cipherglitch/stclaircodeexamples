#This will be the text of get-weather-data.py

#Importing the necessary libraries
import urllib2
from urllib2 import Request
from bs4 import BeautifulSoup
from pprint import pprint
from urllib2 import urlopen
    
#Create/open a file call wunder-data.txt
f = open('wunder-data.txt','w')

#Iterate through the months and days
for m in range(1,13):
    for d in range(1,32):
        
        #Check if already went through month
        if(m==2 and d>28):
            break
        elif(m in [4,6,9,11] and d>30):
            break
            
        #Open wunderground.com URL
        timestamp = '2009-'+str(m)+'-'+str(d)
        print("getting data for "+timestamp)
        url = Request("https://www.wunderground.com/history/daily/KBUF/date/2009-"+str(m)+"-"+str(d), headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url).read()
        
        #Get temperature from page
        soup = BeautifulSoup(page)
        dayTemp = str(soup.findAll(attrs={"class":"ng-star-inserted"}))
        
        #Format month and day strings for output
        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            mStamp = str(m)
            
        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            dStamp = str(d)
            
        timestamp = '2009' + mStamp + dStamp
        
        f.write(timestamp + ',' + dayTemp + '\n')
f.close()