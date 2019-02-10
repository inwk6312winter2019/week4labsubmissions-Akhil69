import string
import matplotlib.pyplot as pyplot
import math
from operator import itemgetter
book_list=[]
book_dict={}
def wrd(word):
	global dic


def test(line):
	for repl in string.punctuation:
		line=line.replace(repl, " ")
	return line
def plot(file):
	dic={}
	fout=open(file,'r')
	for line in fout:
		line=line.strip(string.whitespace+string.punctuation)
		line=test(line)
		for i in line.split():
			dic[i]=dic.get(i,0)+1
	return dic

lst=plot('cobb.txt')

res_lst=[(values,keys) for keys,values in sorted(lst.items())]
res_lst=sorted(res_lst,reverse=True)
pyplot.clf()
pyplot.xscale('log')
pyplot.yscale('log')
pyplot.title('The Zipf graph')
pyplot.xlabel('Rank')
pyplot.ylabel('frequency')
for i in range(2,len(book_list)):
	pyplot.plot(i,i)
pyplot.show()
