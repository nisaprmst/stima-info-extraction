def get_index(word):
    idx = [0] * len(word)
    i = 1
    m = 0
    while i < len(word):
        # kalo sama lanjut
        if word[i].lower() == word[m].lower():
            m += 1
            idx[i] = m
            i += 1
        # kalo beda dan m nya gak 0 ubah m
        elif word[i].lower() != word[m].lower() and m != 0:
            m = idx[m-1]
        # kalo beda dan m = 0 maka index ke i = 0
        else:
            idx[i] = 0
            i += 1
    return idx

def search_keyword_kmp(data, keyword):
    ret = []
    for sentence in data:
        idx = get_index(keyword)
        i = 0
        j = 0
        while j < len(sentence):
            # kalo beda maka update i atau j
            if keyword[i].lower() != sentence[j].lower():
                if i == 0:
                    j += 1
                else:
                    i = idx[i-1]
            # kalo sama increment
            else:
                i += 1
                j += 1
                if i == len(keyword):
                    ret.append(sentence)
                    break
    return ret