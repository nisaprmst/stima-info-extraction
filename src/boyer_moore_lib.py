def init_char_value(word): 
    init = [-1]*256
    for i in range(len(word)): 
        init[ord(word[i])] = i; 
    return init 