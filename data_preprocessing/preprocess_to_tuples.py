import os
import pickle
from list_to_onehot import *
from sent_to_tuples import *
import csv

error_words = []

with open(os.path.dirname(__file__)+"/output/colonLess.txt",'r', encoding='utf-8') as file:
    lines = file.readlines()

with open(os.path.dirname(__file__)+"/output/value_index.pkl", "rb") as value_dict_file:
    value_index_dict = pickle.load(value_dict_file)

with open(os.path.dirname(__file__)+"/output/index_value.pkl", "rb") as index_dict_file:
    index_value_dict = pickle.load(index_dict_file)

def str_sent_to_index_sent(line:str):
    words_list = line.split()
    index_sent = []
    
    for word in words_list:
        try:
            index_sent.append(value_index_dict[word])
        except KeyError:
            error_words.append(word)
    return index_sent

with open("tupledata.csv",'w', newline='') as f:
    csvwriter = csv.writer(f)
    header = ['no','x','y']
    csvwriter.writerow(header)
    n = 0
    for line in lines:
        index_sent = str_sent_to_index_sent(line)
        tuples_list = sent_to_tuple(index_sent)
        rows = []
        for tup in tuples_list:
            if (tup[0] == [] or tup[1] == []):
                continue
            else:
                n += 1
                rows.append([n,tup[0],tup[1]])
        csvwriter.writerows(rows)