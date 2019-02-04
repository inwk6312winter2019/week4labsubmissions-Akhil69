import string
def test():
    fin = open("file","r")
    punct = string.punctuation
    for i in fin:
        i = i.strip().replace(" ","\n")
        for j in punct:
           i = i.replace(c,"").lower() 
        print(i)
test()
