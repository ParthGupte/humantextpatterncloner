import pickle
import os
import re

words = []
index_values = {}
values_index = {}

index_count = 0

with open(os.path.dirname(__file__) +'\output\colonLess.txt', 'r', encoding="utf8") as file1:
    lines = file1.readlines()
    # print (lines[10].split())

    for i in range(0, len(lines)):
        line = lines[i].strip()
        line = line.split()
        for j in range(0, len(line)):


            conv_to_string = str(line[j]) 
            #convert to string
            words.append(conv_to_string)
            # res = re.sub(r'[^\w\s]', '', conv_to_string) 
            #regex for removing punctuation 
            # if res != '':
            #     words.append(res)
    words = [*set(words)]
    print(words)

for i in range(0, len(words)):
    index_values[i] = words[i]
    values_index[words[i]] = i

    # for i in range(0, len(lines)):
    #     line = lines[i].strip()
    #     print(line.split())
    #     index_values[i] = line
    #     values_index[line] = i

with open (os.path.dirname(__file__) +'\\output\\index_value.pkl', 'wb') as file2:
    pickle.dump(index_values, file2)

with open (os.path.dirname(__file__) +'\\output\\value_index.pkl', 'wb') as file3:
    pickle.dump(values_index, file3)

