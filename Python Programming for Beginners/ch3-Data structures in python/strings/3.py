nameList=[]
for i in range(0,10):
    names=input()
    nameList.append(names)

for i in range(0,10):
	nameList[i] = nameList[i][0].upper() + nameList[i][1:].lower()

for i in range(0,10):
    names=nameList[i]
    print(names)

    