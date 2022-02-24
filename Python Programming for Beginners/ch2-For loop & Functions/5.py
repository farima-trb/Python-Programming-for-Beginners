ages=[]
age=int(input())
while age!=-1 and age>=10 and age<=90:
    ages.append(age)
    age=int(input())
    while age!=-1 and age>=10 and age<=90:
        ages.append(age)
        age=int(input())

ages.sort()
print(ages[-1],ages[-2])