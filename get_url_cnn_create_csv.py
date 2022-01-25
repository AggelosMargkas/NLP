##### Aggelos Margkas ##############
####Ergasia Glossiki Texnologia ####
####    20/01/2022    ##############
####################################

##### Step 1 ######

# Gia to web scrapping xrisimopoiounte oi vivliothikes urllib kai Beautifuloup
#Auto einai to initial arxeio. Prwta ginetai katharisma ginetai web scrapping gia na parw ta link pou me endiaferoun kai ola auta
#ta pernaw sto CNN.csv arxeio

#### Step 2 #####
# file: url_article_pair_cnn.py


import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

URL = "https://edition.cnn.com"
basique_url = "https://edition.cnn.com"
site = uReq(URL)
rawPage = site.read()
soup = BeautifulSoup(rawPage, 'html.parser')
site.close()
urls_daily_mail_tabs = []
article_url_daily_mail = []
dataFrame = []
frame = []
text = soup.find_all("ul",  class_ = 'sc-cSHVUG gWEcfQ')

print(text)

for ul in text:
    for litag in ul.find_all("li"):
        if re.match(r"/+", litag.a.get("href")):
             print(litag.a.get("href"))
             l = basique_url + str(litag.a.get("href"))
             urls_daily_mail_tabs.append(l)
             print(l)


for every_link in urls_daily_mail_tabs:

    tag_url = uReq(every_link)
    rawPage = tag_url.read()
    soupa = BeautifulSoup(rawPage, 'html.parser')
    site.close()

    get_h2 = soupa.find_all('h3', class_ = 'cd__headline')
    for article_url in get_h2:

            if(article_url.a is not None):

                    if re.match( r'http+',   article_url.a.get("href")) is None :
                        article_url_daily_mail.append(basique_url + article_url.a.get("href"))
                        print("hola kosme")

out_filename = "CNN.csv"

f=open(out_filename, "w", encoding='utf-8')
headers="idLink"
f.write(headers + "\n")

for link in article_url_daily_mail:
     f.write(link + "\n")

f.close()

