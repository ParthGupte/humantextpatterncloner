import pickle
import os

index_values = {}
values_index = {}

with open(os.path.dirname(__file__) +'\output\colonLess.txt', 'r', encoding="utf8") as file1:
    lines = file1.readlines()

    for i in range(0, len(lines)):
        line = lines[i].strip()
        index_values[i] = line
        values_index[line] = i

with open (os.path.dirname(__file__) +'\\output\\index_value.pkl', 'wb') as file2:
    pickle.dump(index_values, file2)

with open (os.path.dirname(__file__) +'\\output\\value_index.pkl', 'wb') as file3:
    pickle.dump(values_index, file3)

