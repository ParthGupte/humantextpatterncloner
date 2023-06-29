import pickle
with open('value_index.pkl', 'rb') as f:
    while True:
        try:
            line = pickle.load(f)
            print(line)
        except EOFError:
            # Reached end of file
            break