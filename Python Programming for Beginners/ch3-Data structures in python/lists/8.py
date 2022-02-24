destination=input()
d=destination.split()
for i in range(0,3):
    d[i]=int(d[i])

print(max(d)-min(d))