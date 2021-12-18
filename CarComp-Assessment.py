#Content of the get-weather-data.py
# This script below gets the data for every day of a given year.
#Company cars: 2019 Escape, 2019 CRV, 2019 Santa Fe, 2019 RAV4
#Company Eval Points:
#    Safety Features(10)


#    Maintenance Cost(5)

#    Price Point(7)
#edm-comparator-pricing > div > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(2) Escape
#edm-comparator-pricing > div > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(2) CRV
#edm-comparator-pricing > div > div:nth-child(2) > div > div:nth-child(3) > div > div:nth-child(2) Santa Fe
#edm-comparator-pricing > div > div:nth-child(2) > div > div:nth-child(4) > div > div:nth-child(2) RAV4

#Safety

#Maintenance

import urllib.request
import bs4 as bs
from pprint import pprint

from urllib.request import Request, urlopen

#class AppURLopener(urllib.request.FancyURLopener):
#    version = "Mozilla/5.0"
#    
#opener = AppURLopener()
#response = opener.open('http://httpbin.org/user-agent')
#Create/open file called wunder-data.txt
##f = open('auto-data.txt','w')

#Opening each website
url = Request("https://www.cars.com/research/compare/?acodes=USC90TOS111A0,USC90HYS011A0,USC90FOS131A0,USC90HOS021A0", headers={'User-Agent':'Mozilla/5.0'})
page = urlopen(url).read()

#Creating the soup
soup = bs.BeautifulSoup(page, "html.parser")

#This will get the data points from the websites.
carName = soup.findAll(attrs={"class":"listing-name"})
carPrice = soup.findAll(attrs={"format":"currency"})
##carMaint = soup.findAll(attrs={"data-test":"feature 5-Year Ownership Costs Maintenance"})
##carSafety = soup.findAll(attrs={"class":"carSafety"})
#This will be the output for the CSV file
##for i in range(0,3):
##    f.write(carName[i].text + ',' + carPrice[i].text)
##f.close()
##print (carName)
##print (carPrice)
##print (carMaint)
##print (carSafety)
for i in range (0,4):
##    print (carName[i].text)
    print (carPrice[i].text)
