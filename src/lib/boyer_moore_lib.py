def init_char_value(word): 
    init = [-1]*256
    for i in range(len(word)): 
        init[ord(word[i])] = i; 
    return init 

def search_keyword_bm(data, keyword):
    ret = []
    key_length = len(keyword)
    val = init_char_value(keyword)
    for sentence in data:
        sen_length = len(sentence)
        i = 0
        while(i <= sen_length - key_length):
            j = key_length - 1
            while j >= 0 and sentence[i+j].lower() == keyword[j].lower():
                j -= 1
            if j == -1:
                ret.append(sentence)
                if i + key_length < sen_length:
                    i += key_length - val[ord(sentence[i+key_length])]
                else:
                    i += 1
            else:
                i += j - val[ord(sentence[i+j])]
                if i <= 0:
                    i = 1
    return ret
