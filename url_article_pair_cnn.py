##### Aggelos Margkas ###############
#### Ergasia Glossiki Texnologia ####
####    20/01/2022    ###############
#####################################

##### Step 2 ######

# Sto arxeio auto diavazete to csv arxeio pou dimiourgithike sto prohgoumeno vima kai stin sinexeia
# ginetai anoigma kai parse autwn twn selidwn me stoxo na parw to text file pou me endiaferei
# Telos o tropos pou metaxirizomai ta dedomena einai me dictionaries giati einai polu eukola
# Na ta metaxeiristw kai na dimiourgisw json arxeia
# Kai gia auto sto telow sximatizetai to CNN.json




#### Step 3 #####
# file: PoStag.py



import csv
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import json

data = {}
file = open('CNN.csv')
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

    print(all_links)
    temp_data = {}
    temp_text = []
    try:
        site = uReq(all_links)
        rawPage = site.read()
    except Exception:
        pass

    soup = BeautifulSoup(rawPage, 'html.parser')

    site.close()

    text = soup.find_all("div", {"class" : "zn-body__paragraph"})
    #print(text)

    for i in text:
        #print(i.getText())
        temp_text.append(i.getText())

    article = ' '.join(temp_text)



    temp_data = {
        "id": all_links,
        "article": article
    }

    data[counter] = temp_data

    counter = counter + 1

print(data)



jsonString = json.dumps(data, indent=4)
jsonFile = open("CNN.json", "w")
jsonFile.write(jsonString)
jsonFile.close()