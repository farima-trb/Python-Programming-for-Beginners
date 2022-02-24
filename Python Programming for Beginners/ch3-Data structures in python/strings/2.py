tinput=input()
tinput=tinput.replace('+','')
tsorted=sorted(tinput)
res=""
res=res.join(tsorted)
res='+'.join(tsorted)
print(res)
