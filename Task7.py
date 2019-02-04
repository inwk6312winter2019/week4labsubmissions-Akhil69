def sed(pattern,replace,file1,file2):
        try:
                fin1=open(file1,'r')
                fin2=open(file2,'w')
        except:
                print('Error!')

        for i in fin:
                i=i.replace(pattern,replace)
                fin2.write(i)
        fin.close()
        fin2.close()

pattern='pattern'
replace='replace'

file1='testfile.txt'
file2=file2+'.replaced'

sed(pattern,replace,filein,fileout)
