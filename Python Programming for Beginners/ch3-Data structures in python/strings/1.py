word=input()
word=word.lower()
# wlist=list(word)
# for i in wlist:
# 	if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
# 		wlist.pop(wlist.index(i))
		

word=word.replace('a','')
word=word.replace('i','')
word=word.replace('e','')
word=word.replace('u','')
word=word.replace('o','')


res=""
res=res.join(word)
if (res==''):
	print(res)
else:
	res='.' + '.'.join(res)
	print(res)

