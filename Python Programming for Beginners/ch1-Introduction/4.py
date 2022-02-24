num = int(input())
if num%10==0:
    num=num+10
    print(num)
else:
    rest=num%10
    rest=10-rest
    print(num+rest)

