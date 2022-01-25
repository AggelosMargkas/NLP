##### Aggelos Margkas ###############
#### Ergasia Glossiki Texnologia ####
####    20/01/2022    ###############
#####################################

##### Step 3 ######

# An kai se auto to arxeio den ginetai oi dimiourgia tou inverted index einai to pio simantiko arxeio
# Se auto to ginontai initialize oi pio vasikes sinartiseis kai o katharismos kai xaraktirismos ton
# text arxeiwn pou exoume apo ta site

# I vasiki vivliothiki pou xrisimopoieite einai oi nltk
# Vasika pragmata pou xrisimopoiounte einai ta state_union gia tin dimiourgia enos train text pou voithaei sto tokenization mazi me to PunktSentenceTokenizer
# Ta stop words gia ton katharismo tous
# Ta wordnet gia ta postags
# To WordNetLemmatizer gia thn dimiourgia enow object lemmatizer to opoio tha dimiourgei ta lemma




#### Step 4 #####
# file: inverted_index.py



import json
import nltk
from nltk.corpus import state_union, stopwords, wordnet
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter
from nltk.stem import WordNetLemmatizer



train_text = state_union.raw("2005-GWBush.txt")
stop_words = stopwords.words("english")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
article_corpus = []
article_id = []
lemmatizer = WordNetLemmatizer()
open_class_category = ["JJ", "JJR", "JJS", "RB", "RBR", " RBS", "NN", "NNS", "NNP", "NNPS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "FW"]
input_file = "dataDailyMail.json"
temp_lemmas = []
f = open(input_file, "r")

data_input_paper = json.load(f)

f.close()

one_article_corpus = data_input_paper["0"]["article"]


#auti i sinartisi voithaei stis lemma
#ftiaxnw ena dictionari oste vasi ton tags
#na ginete to katalilo lemmatization
def get_wordnet_pos(word):

    #pernw to tag tis leksis kai basi autou girnaei to katalilo xaraktiristiko
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


#auti i sinartisi girnaei ola ta upperwords me ta to prwto gramma kefalaio giati polla itan stin arxi ths
#protasis kai itan axristi pliroforia
def add_upper_stopwords():

    with_upper_stop_words = []
    for i in stop_words:

        with_upper_stop_words.append(i)
        upper_first_letter = i[0].upper()

        string_stop_words = i
        string_stop_words = string_stop_words[:0] + upper_first_letter + string_stop_words[1:]

        with_upper_stop_words.append(string_stop_words)

    return with_upper_stop_words


#edw ginete to tokenization
#kai ftiaxnontai kai ta lemma
#katharizw vasi ta stopwords
#katharizw ta punctuations
#girnane kathara kai me ta antistixa tags tous
def tokenize_site(site):


    tokenized = custom_sent_tokenizer.tokenize(site)

    stopWords = add_upper_stopwords()
    listOfTags = []
    combine_sentences = []
    try:
        for i in tokenized:

            #tokenize kathe protasi
            words = nltk.word_tokenize(i)
            #katharizoume ta punctuations pou den mas dinoun kamia pliroforia kai ta grammata pou menoun mona tous
            words = [word for word in words if word.isalpha() and len(word) > 1]

            #pairnoume tis limmes gia kathe leksi vasi tou tag tous
            lemmatized_words = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in words]

            #sindew oles tis protaseis se mia lista
            combine_sentences.extend(lemmatized_words)

        #pername ta tags gia kathe leksi pou perase sti lista
        tagged = nltk.pos_tag(combine_sentences)

        #print(tagged)

        for j in tagged:
          if j[0] not in stopWords:
               listOfTags.append(j)

        return listOfTags

    except Exception as e:
        print(str(e))



#edw filtrarontai ta clossed class category tag
#ousiastika pernw mono auta pou mou einai xrisima
def filter_clossed_class_category_tag(corpus):
    try:

            filteredWords = []
            tokenizedText = tokenize_site(corpus)

            for i in tokenizedText:

                if i[1] in open_class_category:
                    filteredWords.append(i[0])

            return filteredWords

    except Exception as e:
        print(str(e))


#edw vlepoume me xrisi tis vivliothiki Counter
#poses fores emfanizontai ta lemma mes to keimeno
def word_frequency(article):
    l = Counter(list(filter_clossed_class_category_tag(article)))
    return Counter(l)



#Auti i sinartisi pairnei san eisodo ena dictionary kai ta xaraktiristika enow lemma kai ta prosthetei
#dedomenou oti to lemma auto den iparxei mesa sto dictionary
def add_new_lemma_dictionary(dict, lemma, id, weight):
    temp_data_lemma = {0: {'document_id': id, 'weight': weight}}
    dict[lemma] = temp_data_lemma

    return dict


#Antisoixa i sinartisi auti pairnei ta idia orisisma alla me dedomeno oti to lemma
#Uparxei sto dictionary ara o stoxos tou einai na min dimiourgisei kainourgio key
#me onoma to lemma alla na kanei add to tf-df
#Den ginetai kapoio eidous sort auto ginetai mono sto arxeio Evaluate_Inverted_Index.py
def add_existed_lemma_dictionary(dict, lemma, id, weight):

    temp = {'document_id': id, 'weight': weight}
    index = str(len(dict[lemma]))
    dict[lemma][index] = temp

    return dict




