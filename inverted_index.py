##### Aggelos Margkas ###############
#### Ergasia Glossiki Texnologia ####
####    20/01/2022    ###############
#####################################

##### Step 4 ######

#Meta apo to PoStag.py ginetai i dimiourgia tou inverted_index.py
#Se auton ton fakelo ginetai apla implementation twn sinartisewn poy
#ulopoithikan

#Diavazontai ta json se dictionary etsi wste na exoume to id kai to text gia kathe site
#Ginetai o ipologismo to tf-idf manually kai xwris sinartisi
#I ulopoiisi me sinartisi epivarine parapano ti taxitita twn iterations
#Stin sinexeia elegxetai an to lemma iparxei i oxi ston inverted_index dictionary
#kai pratei analoga me tis sinartiseis pou oristikan sto PoStag.py
#Telos to dictionary pernaei stin morfi json ston fakelo InvertedIndex.json


#### Step 5 #####
# file: Evaluate_Inverted_Index.py


from PoStag import *
import json
import math


inverted_index = {}
input_file = ["CNN.json", "dataDailyMail.json"]

f = open("dataDailyMail.json", "r")

data_input_paper = json.load(f)


for news_site in input_file:

    f = open(news_site, "r")

    data_input_paper = json.load(f)

    f.close()

    lenght = len(data_input_paper)
    for i in data_input_paper:
        cleaned_words = filter_clossed_class_category_tag(data_input_paper[i]["article"])
        id_words = data_input_paper[i]["id"]


        size_lemmas = len(cleaned_words)
        print("Arxeia pou mpika " + i + " apo ta " + str(lenght) + "\n")
        for leksi in cleaned_words:

            freq = cleaned_words.count(leksi)
            tf = freq / size_lemmas
            idf = 10 * math.log(size_lemmas/(freq + 1))
            tf_idf = tf*idf


            if leksi not in inverted_index.keys():
                add_new_lemma_dictionary(inverted_index, leksi, id_words, tf_idf)
            else:
                add_existed_lemma_dictionary(inverted_index,leksi, id_words, tf_idf)


jsonString = json.dumps(inverted_index, indent=4)
jsonFile = open("InvertedIndex.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
