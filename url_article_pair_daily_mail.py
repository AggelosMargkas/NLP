##### Aggelos Margkas ###############
#### Ergasia Glossiki Texnologia ####
####    20/01/2022    ###############
#####################################

##### Step 2 ######

# Sto arxeio auto diavazete to csv arxeio pou dimiourgithike sto prohgoumeno vima kai stin sinexeia
# ginetai anoigma kai parse autwn twn selidwn me stoxo na parw to text file pou me endiaferei
# Telos o tropos pou metaxirizomai ta dedomena einai me dictionaries giati einai polu eukola
# Na ta metaxeiristw kai na dimiourgisw json arxeia
# Kai gia auto sto telow sximatizetai to DailyMail.json


#Oi vivliothikes pou prosthethikan einai oi csv kai json gia read kai write fakelwn

#### Step 3 #####
# file: PoStag.py

import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import json


data = {}

file = open('DailyMail.csv')
type(file)

csvreader = csv.reader(file)

column_links = []

header = []
header = next(csvreader)
print(header)

for i in csvreader:
    column_links.extend(i)

print(column_links)

counter = 0
for all_links in column_links:

    temp_data = {}
    temp_text = []
    site = uReq(all_links)
    rawPage = site.read()

    soup = BeautifulSoup(rawPage, 'html.parser')

    site.close()

    text = soup.find_all("p", {"class" : "mol-para-with-font"})
    title = soup.get("script")

    for i in text:
        temp_text.append(i.getText())

    article = ' '.join(temp_text)

    temp_data = {
        "id": all_links,
        "article": article
    }

    data[counter] = temp_data

    print("\n \n")
    print(data)
    counter = counter + 1

print(data)

jsonString = json.dumps(data, indent=4)
jsonFile = open("dataDailyMail.json", "w")
jsonFile.write(jsonString)
jsonFile.close()