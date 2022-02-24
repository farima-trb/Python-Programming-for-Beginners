number=int(input())
idlist=[]
for i in range(0,number):
	id=input()
	idlist.append(id)
	idlist[i]=id.split()


for i in range(0,number):
	for j in range(0,2):
		idlist[i][j]=int(idlist[i][j])

idlist.sort()        

qualities=[]
unsorted_qualities=[] 

for i in range(0,len(idlist)):
	qualities.append(idlist[i][1])

for i in range(0,len(qualities)):
	unsorted_qualities.append(qualities[i])

qualities.sort()

if qualities!=unsorted_qualities:
	print('happy irsa')
else:
	print('poor irsa')