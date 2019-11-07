import bs4 as bs
import urllib.request
import pandas as pd
import codecs
import re
import csv

##url = "H:\google drive folder\python\projects\web scraper\sites\Dose-Ranging Study of Recombinant AAV2_6 Human Factor 8 Gene Therapy SB-525 in Subjects With Severe Hemophilia A - Full Text View - ClinicalTrials.gov.html"
##url = "C:\\Users\\dongh\\Documents\\Google Drive\\python\\projects\\web scraper\\sites\\Dose-Ranging Study of Recombinant AAV2_6 Human Factor 8 Gene Therapy SB-525 in Subjects With Severe Hemophilia A - Full Text View - ClinicalTrials.gov.html"
##f=codecs.open(url, 'r', 'utf-8')
##soup = bs.BeautifulSoup(f, 'lxml')
##print (soup)
##print("****************************************************************************************")

## website request
url = "https://clinicaltrials.gov/ct2/show/NCT03061201"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
sauce = urllib.request.urlopen(req).read()
soup = bs.BeautifulSoup(sauce, 'lxml')


###gets url
##sauce = urllib.request.urlopen("https://clinicaltrials.gov/ct2/show/NCT03061201?term=sb+525&rank=1").read()
###parses into HTML
##soup = bs.BeautifulSoup(sauce, 'lxml')



matches =[]
string = ""
def search(soup):
    global matches
    global string
    for td in soup.select('td[headers]'):
        for items in td["headers"], td.get_text(strip=True):
            if "Recruiting" or "Withdrawn" in items:
                matches.append(items)

search(soup)
print(matches)
print(type(matches))
print(len(matches))
print("****************************************************************************************")

print(string)

string = "".join(str(matches))
print(string)

print(type(string))
print("****************************************************************************************")


split = re.findall("Recruiting|Withdrawn", string)

split2 = re.findall("\['locName'\](.*?)\['locStatus'\]", string)

print(split)
print(len(split))
print(split2)
print(len(split2))

split2 = [items.replace(",", '') for items in split2]
split2 = [items.replace("'",'') for items in split2]
split2 = [items.replace("\"",'') for items in split2]



print("****************************************************************************************")

## stores lists (split, split2) as coumns and names them
df = pd.DataFrame(list(zip(split2, split)), columns = ["hospitals", "Status"])

print(df)

##stores lists in a csv file
df.to_csv("clinical trials.csv", index = True)
