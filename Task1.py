import string
def test():
    """Here code reads,breaks the file(whitespace) and convertingwords to lowercase"""
    fin = open("58782-0(1).txt","r")
    pun_char = string.punctuation
    for i in fin:
        i = i.strip().replace(" ","\n")
        for char in pun_char:
           i = i.replace(char,"")
        i = i.lower()
        print(i)
test()
