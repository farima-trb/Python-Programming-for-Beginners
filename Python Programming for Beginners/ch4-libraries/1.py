import math
numbers=int(input())
numList=[]
for i in range(0,numbers):
    num=int(input())
    num=math.sqrt(num)
    numList.append(num)

for i in range(0,numbers):
    print(str('%.10f'%numList[i])[:-6])
    