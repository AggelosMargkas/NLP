##### Aggelos Margkas ##############
####Ergasia Glossiki Texnologia ####
####    20/01/2022    ##############
####################################

##### Step 3 ######

# Auto einai to teleutaio arxeio estiazei stin dimiourgia ton sparse vector gia kathe text
# mesa sto dataset "20 news groups corpus"
# I vasiki vivliothiki pou ulopoiithike gia auto to erwtima einai sklearn
# I opoia parexei mia megali eukolia gia tin metrisi tis apostasis dianismatwn
# Xreiastika kai oi pandas kai oi numpy gia tin dimiourgia dataset apothikeusis twn dedomenwn
# kai gia tin diaxeirisi matrixes antistoixa
# Se autin tin sinartisi ftiaxnetai enas vectonizes TfidfVectorizer o opoios apoteleitai apo dio xaraktiristika
# To proto einai to leksilogio pou to pernoyme apo to sunolo S to opio dimiourgithike sto
# arxeio char_space.py kai apo stemming process to opio ginetai stin sinartisi stemming_tokenizer()
# Kai gia ta dio json files pou ftiaxtika gia ta antistoixa set ginetai to diavasma tous kai
# Epeleksa na epilegontai 8000 xaraktiristika opws sto paradeigma stin ekfonisi gia matrixes me tis times ton tf-df

from char_space_S import *
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import pandas as pd
from nltk.stem.porter import PorterStemmer
import re
import numpy as np



stemmer = PorterStemmer()

sinolo_S = get_S()

print("Ftiaxtike to sinolo S megethos 8000\n")

def stemming_tokenizer(str_input):
    words = re.sub(r"[^A-Za-z0-9\-]", " ", str_input).lower().split()
    words = [stemmer.stem(word) for word in words]
    return words

f = open('Sullogh_E.json')

data_silogis_E = json.load(f)

print("Diavasa to Sunolo E \n")
f = open('Sullogh_A.json')

data_silogis_A = json.load(f)
print("Diavasa to Sunolo  \n")


text_examples_E = []
text_examples_A = []
id_A = []
katigories_index = []



for topic in thematikes_katigories:
    for i in data_silogis_E[topic]:
        a_text = i["text"]
        text_examples_E.append(a_text)
        katigories_index.append(topic)

    for j in data_silogis_A[topic]:
        b_text = j["text"]
        id_A.append(j["id"])
        text_examples_A.append(b_text)

print("Pira ta tf-idf kai gia ta dio sinola \n")

vectorizer = TfidfVectorizer(vocabulary=sinolo_S,
                                     tokenizer=stemming_tokenizer)

response_e = vectorizer.fit_transform(text_examples_E)
response_a =vectorizer.fit_transform(text_examples_A)
print("Eftiaksa dianismata kai gia ta dio sinola \n")



cosine = cosine_similarity(response_a[0:], response_e[0:])
print("Pira tin prwti apostasi gia cosine \n")
euclidean = euclidean_distances(response_a[0:], response_e[0:])
print("Pira tin deuteri apostasi gia euclidean \n")

counter1 = 0
counter2 = 0
dataframe_list_cosine = {}
dataframe_list_euclidean = {}
test_article = []
test_katigories = []


for iii in cosine:
    temp_list = []
    l = np.where(iii == max(iii))

    test_article.append(id_A[counter1])
    test_katigories.append(katigories_index[l[0][0]])
    counter1 = counter1 + 1

dataframe_list_cosine = {
    "File": test_article,
    "Katigoria": test_katigories}



df_tfidfvect = pd.DataFrame(data=dataframe_list_cosine)


filename = "Categorize_Cosine.xlsx"

df_tfidfvect.to_excel(filename)
print('DataFrame gia cosine perase sto Excel File me epitixia! \n')




for iii in euclidean:
    temp_list = []
    l = np.where(iii == max(iii))
    #print("To eggrafo " + id_A[counter2] + " anoikei stin katigoria " + katigories_index[l[0][0]])

    test_article.append(id_A[counter2])
    test_katigories.append(katigories_index[l[0][0]])
    counter2 = counter2 + 1

dataframe_list_euclidean = {
    "File": test_article,
    "Katigoria": test_katigories}



df_tfidfvect = pd.DataFrame(data=dataframe_list_euclidean)


filename = "Categorize_Euclidean.xlsx"

df_tfidfvect.to_excel(filename)
print('DataFrame gia euclidean perase sto Excel File me epitixia! \n')


print(euclidean - cosine)