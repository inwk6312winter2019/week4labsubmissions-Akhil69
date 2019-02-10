import string

fp=open('file.txt')
r=fp.read()

def test_book():
	i=0
	res=dict()
	for ln in r.split():
		st=ln.strip(string.punctuation)
		wrds=st.lower()
		print(wrds)	
		i=i+1
		if wrds not in res:
			res[wrds]=1
		else:
			res[wrds]+=1

	print('words in book',i)
	print(res)
	print('words',len(res))
	lstt=[]
	for key,value in res.items():
		lstt.append((value,key))
	lstt.sort(reverse=True)
	print(lstt)
	for freq,word in lstt[:20]:
		print(word,freq,sep='\t')


test_book()
