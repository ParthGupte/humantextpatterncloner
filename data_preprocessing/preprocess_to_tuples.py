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

f = open("tupledata.csv",'a')
csvwriter = csv.writer(f)
header = ['no','x','y']

n = 0
for line in lines:
    index_sent = str_sent_to_index_sent(line)
    tuples_list = sent_to_tuple(index_sent)
    rows = []
    for tup in tuples_list:
        n += 1
        rows.append([n,tup[0],tup[1]])
    csvwriter.writerows(rows)
f.close()