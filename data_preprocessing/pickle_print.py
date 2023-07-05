import pickle
import os
count = 0
with open(os.path.dirname(__file__)+'/output/index_value.pkl', 'rb') as f:
    # try:
    line = pickle.load(f)
    print(line)
    count +=1
    # except EOFError:
        # Reached end of file
        # print("nigga nigga nigga")
        # break