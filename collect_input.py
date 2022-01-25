##### Aggelos Margkas ##############
####Ergasia Glossiki Texnologia ####
####    20/01/2022    ##############
####################################

##### Step 2 ######

# To arxeio auto diavazei ta sinola E kai A
# Xrisimopoiountai oi idies vivliothikes me prin
# Ta arxeia perniountai sta arxeia Sullogh_E.json kai Sullogh_A.json
# To mono pou diaferei to diavasma einai oti stin periptwsi tou E to
# Kai se auto ginetai mia mikri proepeksergasia wste na katharistoun
# punctuations, stoprwords kai lekseis megethous enos grammatos
# Wste to tf-idef ustera na exei pio akrivis timi

#### Step 3 #####
# file: Dianismata_Xaraktiristikwn.py



import json
from pathlib import Path
import os
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

stop_words = stopwords.words("english")
stemmer = PorterStemmer()
Sullogh_E = {}
Sullogh_A = {}
thematikes_katigories = []


entries = Path('C:/Users/junio/IdeaProjects/NLP/20news-bydate-test/')
for entry in entries.iterdir():
    thematikes_katigories.append(entry.name)


#Kataskeui Sinolou E
for katigoria in thematikes_katigories:

    Sullogh_E[katigoria] = {}
    temp_array_E = []

    for filename in os.listdir("C:/Users/junio/IdeaProjects/NLP/20news-bydate-train/" + katigoria +"/"):
       with open(os.path.join("C:/Users/junio/IdeaProjects/NLP/20news-bydate-train/" + katigoria +"/", filename), 'r') as f:

            text = f.read().lower()
            temp_text = []
            tokens = text.split()
            words = [word for word in tokens if word.isalpha() and len(word) > 1 and word not in stop_words]
            temp = {"id": filename,
                    "text": ' '.join(words)}
            temp_array_E.append(temp)

    Sullogh_E[katigoria] = temp_array_E


#Kataskeui Sinolou A
for katigoria in thematikes_katigories:

        Sullogh_A[katigoria] = {}
        temp_array_A = []

        for filename in os.listdir("C:/Users/junio/IdeaProjects/NLP/20news-bydate-test/" + katigoria +"/"):
           with open(os.path.join("C:/Users/junio/IdeaProjects/NLP/20news-bydate-test/" + katigoria +"/", filename), 'r') as f:

                text = f.read()
                temp = {"id": filename ,
                        "text": text}
                temp_array_A.append(temp)

        Sullogh_A[katigoria] = temp_array_A

print(Sullogh_A)



jsonStringE= json.dumps(Sullogh_E, indent=4)
jsonFile = open("Sullogh_E.json", "w")
jsonFile.write(jsonStringE)
jsonFile.close()

jsonStringA= json.dumps(Sullogh_A, indent=4)
jsonFile = open("Sullogh_A.json", "w")
jsonFile.write(jsonStringA)
jsonFile.close()

print(len(Sullogh_E))