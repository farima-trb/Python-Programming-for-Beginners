entry=input()
count_s=0
count_c=0

for i in range(0,len(entry)):
	if ord(entry[i])<=90 and ord(entry[i])>=65:
		count_c+=1

for i in range(0,len(entry)):
    if ord(entry[i])<=122 and ord(entry[i])>=97:
	    count_s+=1

if (count_c > count_s):
    entry=entry.upper()
    print(entry)
else:
    entry=entry.lower()
    print(entry)     