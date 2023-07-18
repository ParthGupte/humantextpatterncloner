import tensorflow as tf
from tensorflow import keras as ke
import numpy as np

vocab_size = 23940
dim = 200

def word2vec(vocab_size = vocab_size,h_size = dim):
    model = ke.Sequential()
    model.add(ke.layers.Dense(h_size, input_shape = (vocab_size,)))
    model.add(ke.layers.Dense(vocab_size,activation = ke.activations.softmax))
    return model

def encode_tup(tup):
    s = ""
    tup[0].sort()
    tup[1].sort()
    for x in tup[0]:
        if x != tup[0][-1]:
            s += str(x) + "_"
        else:
            s += str(x)
    s += "-"
    for y in tup[1]:
        if y != tup[1][-1]:
            s += str(y) + "_"
        else:
            s += str(y)
    return s

def decode_tup(string_tup):
    x_str, y_str = string_tup.split("-")
    x_str_lst = [int(x) for x in x_str.split("_")]
    y_str_lst = [int(y) for y in y_str.split("_")]
    return (x_str_lst, y_str_lst)

def make_reduced_model(in_out_tuple,model):
    in_out_tuple[0].sort() #sorting for later naming reasons
    in_out_tuple[1].sort()
    in_layer,out_layer = model.layers
    in_params = in_layer.get_weights()
    out_params = out_layer.get_weights()
    
    in_lst,out_lst = in_out_tuple
    
    in_weights = in_params[0][in_lst] #shape (2,200)
    in_bias = in_params[1] #shape (200,)
    out_weights = out_params[0][:,out_lst] #shape (200,1)
    out_bias = out_params[1][out_lst] #shape (1,)
    
    reduced_model = ke.Sequential()
    reduced_model._name = encode_tup(in_out_tuple)
    #making layers of the shapes of the extracted parameters
    h_layer = ke.layers.Dense(in_weights.shape[1], input_shape=(in_weights.shape[0],))
    out_layer = ke.layers.Dense(out_weights.shape[1], ke.activations.softmax)
    reduced_model.add(h_layer)
    reduced_model.add(out_layer)

    
    #setting weights
    reduced_model.layers[0].set_weights([in_weights,in_bias])
    reduced_model.layers[1].set_weights([out_weights,out_bias])
    reduced_model.compile(loss="categorical_crossentropy",optimizer='adam', metrics=['accuracy'])
    return reduced_model

def update_word2vec(reduced_model, model):
    in_out_tuple = decode_tup(reduced_model.name)
    
    in_layer,out_layer = model.layers
    in_params = in_layer.get_weights()
    out_params = out_layer.get_weights()
    
    in_lst,out_lst = in_out_tuple
    
    in_weights, in_bias = in_params
    out_weights, out_bias = out_params
    
    reduced_in_layer, reduced_out_layer = reduced_model.layers
    reduced_in_params = reduced_in_layer.get_weights()
    reduced_out_params = reduced_out_layer.get_weights()
    
    reduced_in_weights, reduced_in_bias = reduced_in_params
    reduced_out_weights, reduced_out_bias = reduced_out_params
    
    #changing weights
    in_weights[in_lst] = reduced_in_weights #replace rows
    in_bias = reduced_in_bias #replace all of it
    out_weights[:,out_lst] = reduced_out_weights #replace columns
    out_bias[out_lst] = reduced_out_bias #replace parts of 1d array
    
    #update word2vec
    in_layer.set_weights([in_weights,in_bias])
    out_layer.set_weights([out_weights,out_bias])
    assert (model.layers[0].get_weights()[0] == in_layer.get_weights()[0]).all()
    
    return model

#training

def create_batch_model(tuples_batch,model):
    in_nodes = []
    out_nodes = []
    for tups in tuples_batch:
        for x in tups[0]:
            if x not in in_nodes:
                in_nodes.append(x)
        for y in tups[1]:
            if y not in out_nodes:
                out_nodes.append(y)
    batch_model_tup = (in_nodes,out_nodes)
    batch_model = make_reduced_model(batch_model_tup,model)
    return batch_model

def create_special_onehot(token_lst,ref_lst):
    n = len(token_lst)
    onehot = np.zeros((len(ref_lst),))
    for i in token_lst:
        onehot[ref_lst.index(i)] += 1
    return onehot/n

def create_tup_onehots(tuples_batch,batch_model_name):
    ref_X, ref_Y = decode_tup(batch_model_name)
    X_lst = []
    Y_lst = []
    for tup in tuples_batch:
        x_onehot = create_special_onehot(tup[0],ref_X)
        y_onehot = create_special_onehot(tup[1],ref_Y)
        
        X_lst.append(x_onehot)
        Y_lst.append(y_onehot)
    X = np.array(X_lst)
    Y = np.array(Y_lst)
    return X, Y

def train_on_tup_batch(tuples_batch,model):
    batch_model = create_batch_model(tuples_batch,model)
    X, Y = create_tup_onehots(tuples_batch,batch_model.name)
    batch_model.train_on_batch(X,Y)
    update_word2vec(batch_model,model)
    
# # create_special_onehot([1,2,4],[1,2,3,4,5])
# tups_batch = [([1,2],[4]),([2,4],[3]),([1,4],[3])]
# train_on_tup_batch(tups_batch,word2vec_model)
# batch_model = create_batch_model(tups_batch,word2vec_model)
# print(batch_model.name)
# create_tup_onehots(tups_batch,batch_model.name)
# e = encode_tup(tups_batch[0])
# print(decode_tup(e))