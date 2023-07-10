import pickle
import os
with open(os.path.dirname(__file__)+'/output/index_value.pkl', 'rb') as f:
    # try:
    
    line = pickle.load(f)
    print(line)
    # except EOFError:
        # Reached end of file
        # print("nigga nigga nigga")
        # break