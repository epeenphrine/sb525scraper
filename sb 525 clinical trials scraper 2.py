import bs4 as bs
import urllib.request
import pandas as pd
import codecs
import re
import csv

############# offfline testing
##url = "htmlfilenamehere"
##
##f=codecs.open(url, 'r', 'utf-8')
##soup = bs.BeautifulSoup(f, 'lxml')
##print (soup)
##print("****************************************************************************************")




## website request
url = "https://clinicaltrials.gov/ct2/show/NCT03061201"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
sauce = urllib.request.urlopen(req).read()
soup = bs.BeautifulSoup(sauce, 'lxml')



## parse through elements in HTML.
matches =[]
string = ""
def search(soup):
    global matches
    global string
    for td in soup.select('td[headers]'):
        for items in td["headers"], td.get_text(strip=True):
            if "Recruiting" or "Withdrawn" in items:
                matches.append(items)
## checking for lists if enrollment pressent
matches2 = []
def search2(matches):
    global matches2
    for items in matches:
        if "participants" in items:
            matches2.append(items)
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

## uses regex to split string into keywords and store in a list. one list for enrollment status and other for hospital name.
split = re.findall("Recruiting|Withdrawn", string)

split2 = re.findall("\['locName'\](.*?)\['locStatus'\]", string)

### cleans hospital names. Removes characters: , ' "
split2 = [items.replace(",", '') for items in split2]
split2 = [items.replace("'",'') for items in split2]
split2 = [items.replace("\"",'') for items in split2]

print(split)
print(len(split))
print(split2)
print(len(split2))

print("****************************************************************************************")

## stores lists (split, split2) as coumns and names them
df = pd.DataFrame(list(zip(split2, split)), columns = ["hospitals", "Status"])

print(df)
### stores lists in a CSV file
df.to_csv("clinical trials2.csv", index = True)

