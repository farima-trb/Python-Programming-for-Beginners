num=int(input())
rest1=num%10
rest2=((num//10)%10)
rest3=((num//10)//10)
num1=str(rest1)+str(rest2)+str(rest3)
num1=2*int(num1)
print(num1)