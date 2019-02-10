import string
def test():
    fin = open("file.txt","r")
    p = string.punctuation
    res = dict()
    i = 0
    word_list = []
    for i in fin:
        i = i.strip()
        for j in p:
           i = i.replace(j,"")
        i = i.lower()
        k = i.split()
        for lst in k:
            word_list.append(lst)
    for ls in word_list:
        if ls not in res:
            res[ls] = 1
        else:
            res[ls] += 1
    for key, value in res.items():
        if(value == 20):
            print(key)

test()


