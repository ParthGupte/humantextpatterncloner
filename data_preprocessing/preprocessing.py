#fetch the dict
#convert each line to token
#sent_to_token on each line
#convertInputToOneHotPercentages on each element of tuple

import csv
import pickle
from list_to_onehot import *
from sent_to_tuples import *

file = open("output/colonLess.txt")
csvreader = csv.reader(file)

index_dict_file = open("output/index_value.pkl")
value_dict_file = open("output/value_index.pkl")

index_value_dict = pickle.load(index_dict_file)
value_index_dict = pickle.load(value_dict_file)

index_dict_file.close()
value_dict_file.close()

def str_sent_to_index_sent(line:str):
    words_list = line.split()
    index_sent = []
    for word in words_list:
        index_sent.append(value_index_dict[word])
    return index_sent

X_list =  []
Y_list = []

for line in csvreader:
    index_sent = str_sent_to_index_sent(line)
    tuples_list = sent_to_tuple(index_sent)
    for tuple in tuples_list:
        X_list.append(convertInputToOneHotPercentages(tuple[0]))
        Y_list.append(convertInputToOneHotPercentages(tuple[1]))

X_array = np.array(X_list)
Y_array = np.array(Y_list)

np.save("X",X_array)
np.save("Y",Y_array)