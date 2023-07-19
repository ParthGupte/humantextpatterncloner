#fetch the dict
#convert each line to token
#sent_to_token on each line
#convertInputToOneHotPercentages on each element of tuple
import os
import pickle
from list_to_onehot import *
from sent_to_tuples import *

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
    # for word in words_list:
    #     index_sent.append(value_index_dict[word])
    return index_sent

n = 0
count = 0
for line in lines:
    # if count == 1:  only for a small list
        # print("line: ",line)
    index_sent = str_sent_to_index_sent(line)
        # print("index sent: ",index_sent)
    tuples_list = sent_to_tuple(index_sent)
        # print("tuples list: ",tuples_list)
    for tuple in tuples_list:
        x = convertInputToOneHotPercentages(tuple[0],len(value_index_dict))
            # print ("X: ",x)
            # print("tuple0 :",tuple[0])
        y = convertInputToOneHotPercentages(tuple[1],len(value_index_dict))
            # print ("Y: ",y)
            # print("tuple1: ",tuple[1])
        np.save(os.path.dirname(__file__)+"/arraydata/x"+str(n),x)
        np.save(os.path.dirname(__file__)+"/arraydata/y"+str(n),y)
        del x
        del y
        n += 1
    # count+=1 inside the if loop remember

print("error: ",error_words)
# X_array = np.array(X_list)
# Y_array = np.array(Y_list)

# np.save("X",X_array)
# np.save("Y",Y_array)