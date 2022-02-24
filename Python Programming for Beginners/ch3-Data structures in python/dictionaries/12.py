number=int(input())
onlinedict=dict()
words=[]
for i in range(0,number):
    words.append(input())

sentence=input()

for i in range(0,number):
	words[i]=words[i].split()

for i in range(0,number):
    onlinedict[words[i][0]] = words[i][1]

# print(onlinedict)
sentence=sentence.split()
translated=''
for word in sentence:
    translated += onlinedict.get(word,word)+' '    

print(translated)
