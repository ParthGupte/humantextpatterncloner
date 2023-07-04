import numpy as np

# VOCABULARY = np.array(['Hello', 'World', 'Program', 'Game', 'Nural Network','LoL'])
SIZE_OF_VOCABULARY = 5 #len(VOCABULARY)
input_array = np.array([1,4,0])



#Creates One Hot array for the value
def valueToOneHot(value):
    one_hot = np.zeros(SIZE_OF_VOCABULARY)
    one_hot[value] = 1
      
    return one_hot

#combines One Hot arrays and makes percentages eg: 0.5 = 50%, 0.6 = 60% 
def oneHotCombine(input_array):
    len_of_input_array = len(input_array)
    occurence_of_each_world_array = np.zeros(SIZE_OF_VOCABULARY)
    for i in range(0, len_of_input_array):
        occurence_of_each_world_array = np.add(occurence_of_each_world_array,input_array[i])
    combinedOneHot = np.where(occurence_of_each_world_array != 0, occurence_of_each_world_array / len_of_input_array, occurence_of_each_world_array)
    return combinedOneHot

arr_of_inputs_onehot = np.empty((0, SIZE_OF_VOCABULARY)) #creates an empty array to store all the one hot for inputs

for i in input_array:
    oneHotConvert = valueToOneHot(i)
    arr_of_inputs_onehot = np.append(arr_of_inputs_onehot, [oneHotConvert], axis=0)
    #adds all the one hots into the array of inputs


X = oneHotCombine(arr_of_inputs_onehot)
print(X)