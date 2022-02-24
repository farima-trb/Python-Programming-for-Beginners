from collections import OrderedDict
votes=OrderedDict()
voteNum=int(input())
for country in range(0,voteNum):
    country=input()    
    if country in votes:
        votes[country]+=1
    else:
        votes[country]=1 

cKeys=list(votes.items())
cKeys.sort()

for i in range(0,len(cKeys)):
	print(cKeys[i][0],cKeys[i][1])

