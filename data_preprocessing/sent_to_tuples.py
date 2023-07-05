
def sent_to_tuple(sent:list,wind_size = 3,left_bias = True):
    output_list = []
    if wind_size % 2 == 1:
        left = int((wind_size - 1)/2)
        right = left
    else:
        if left_bias:
            left = int(wind_size/2)
            right = left -1
        else:
            right = int(wind_size/2)
            left = right -1

    for i in range(len(sent)):
        l_indx = i - left
        r_indx = i + right
        if l_indx < 0:
            l_indx = 0
        if r_indx > len(sent):
            r_indx = len(sent)
        x = sent[l_indx:i] + sent[i+1:r_indx]
        y = [i]
        output_list.append((x,y))

    return output_list
 

