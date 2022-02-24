sum=0
wnum=0
for i in range(1,31):
    score=int(input())
    sum+=score
    if (score==3):
        wnum+=1
        
print(sum,wnum)