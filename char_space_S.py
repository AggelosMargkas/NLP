##### Aggelos Margkas ##############
####Ergasia Glossiki Texnologia ####
####    20/01/2022    ##############
####################################

##### Step 1 ######

# Sto arxeio auto dimiourgeitai to sinolo S pou ziteitai me megethos 8000
# Gia tin diimiourgia tou ulopoithike mia sinartis get_S()
# Ginetai mia stoixeiwdeis proepeksergasia sta dedomena kai
# Xrisimopoieitai o stemmer PorteStemmer tis vivliothikis
# nltk


#### Step 2 #####
# file: collect_input.py


from pathlib import Path
import os
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


stop_words = stopwords.words("english")
stemmer = PorterStemmer()
temp_S = {}
xaraktiristika_sinolos_S = []
thematikes_katigories = []


entries = Path('C:/Users/junio/IdeaProjects/NLP/20news-bydate-test/')
for entry in entries.iterdir():
    thematikes_katigories.append(entry.name)


#Girnaei to sunolo S me 1:8000 diastasi
def get_S():
    for katigoria in thematikes_katigories:
        for filename in os.listdir("C:/Users/junio/IdeaProjects/NLP/20news-bydate-test/" + katigoria +"/"):
           with open(os.path.join("C:/Users/junio/IdeaProjects/NLP/20news-bydate-test/" + katigoria +"/", filename), 'r') as f:
                text = f.read().lower()
                tokens = text.split()

                words = [word for word in tokens if word.isalpha() and len(word) > 1 and word not in stop_words]


                for t in words:
                    if t in temp_S.keys():
                        temp_S.update({t:temp_S[t]+1})
                    else:
                        temp_S[t] = 1

    dic = {k: v for k, v in sorted(temp_S.items(), key=lambda item: item[1])}

    count = 0
    for i in reversed(dic):
        if count != 8000:
                xaraktiristika_sinolos_S.append(i)
        else:
                break
        count = count + 1

    return xaraktiristika_sinolos_S

