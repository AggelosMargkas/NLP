##### Aggelos Margkas ###############
#### Ergasia Glossiki Texnologia ####
####    20/01/2022    ###############
#####################################

##### Step 5  ######

# Sto arxeio auto ginetai o upologismos twn xronwn gia tin anazitisi lemmatwn mesa
# Sto Inverted_Index. Parakatw uparxoun se sxolia ta test pou ulopoithikan gia kathe plithos lemma
# Oi xronoi metrithikan me tin vivliothiki time




import json
import time

f = open("InvertedIndex.json", "r")
data_input_paper = json.load(f)

mean_time = []


def Average(lst):
    return sum(lst) / len(lst)



#I sinartisi evaluetion pairnei os input ta lemma pou dinontai
# Ksekinaei na metraei o xronos kai ginetai ena try kai catch se periptwsi pou exoume kapoio miss
# Sti periprtwsi pou exei kapoio miss vgazei minima kai ksana zitaei dedomena
# Gia to sort tou dictionary simfona me to value ginetai me thn sinartis sorted kai epidi to
# To theloume se fthinousa seira ginetai reverse sto telos
# Stin periptwsi pou exoume para panw apo ena lemma to sort ginetai sto telow afou prwto ginetai to athroisma
# Me ta upoloipa dictionary
# Episi elefxetai an to url uparxei kai stin periptvsh poy yparxei ginetai to athroisma

def evaluation():
    x = list(map(str, input("Let's evaluate the Inverted Index Structure! Please, give me one lemma: ").split()))

    start_time = time.time()

    try:
        if len(x) == 1:

            result = data_input_paper.get(x[0])
            print(x[0])
            temp_dict_values = {}
            resultt = {k: v for k, v in sorted(result.items(), key=lambda item: item[1]['weight'], reverse=True)}

            for value in resultt:
                temp_dict_values.update({resultt[value]["document_id"] : resultt[value]["weight"]})

            print(temp_dict_values)

        else:

            temp_dict_values = {}

            for i in range(len(x)):
                result = data_input_paper.get(x[i])

                for value in result:

                    doc = result[value]["document_id"]
                    w = result[value]["weight"]
                    if doc not in temp_dict_values.keys():
                        temp_dict_values.update({result[value]["document_id"]: result[value]["weight"]})
                    else:
                        temp_dict_values.update({doc: temp_dict_values[doc] + w})


            resultt = {k: v for k, v in sorted(temp_dict_values.items(), key=lambda item: item[1], reverse=True)}

            print(resultt)

    except Exception:
        print("Kapoio leema den iparxei ston inverted index")
        evaluation()

    print("--- %s seconds ---" % (time.time() - start_time))
    mean_time.append((time.time() - start_time))



###TEST###

#1 LEMMA
# for i in range(20):
#     evaluation()
#
#
# print( "Gia 1 lemma o xronos einai : " +Average(mean_time))

#0.4201449871063232


#2 LEMMA
# for i in range(20):
#     evaluation()
# print( "Gia 2 lemma o xronos einai : " + str(Average(mean_time)))

#0.4500447919291835

#3 LEMMA
# for i in range(30):
#     evaluation()
# print( "Gia 3 lemma o xronos einai : " + str(Average(mean_time)))

#1.4500447919291835

#4 LEMMA
# for i in range(30):
#     evaluation()
# print( "Gia 4 lemma o xronos einai : " + str(Average(mean_time)))

#1.4365613874318345