def func(n):
    count=0
    for i in range(1,n+1):
        if(n % i == 0):
            count+=1
    return count      

numbers,divider,=[],[]

for i in range(1,21):
    num=int(input())
    numbers.append(num)
    divider.append(func(num))
    # rmax=max(res)
    # index=res.index(rmax)

# print(numbers[index],rmax)

res=[list(x) for x in zip(numbers,divider)]
rev_res=res.copy()

for i in range(0,len(rev_res)):
    temp=rev_res[i][0]
    rev_res[i][0]=rev_res[i][1]
    rev_res[i][1]=temp

rev_res.sort()

# print('numbers:\n',numbers)
# print('res:\n',divider)
# print('res:\n',res)
# print('reverse res:\n',rev_res)

print(rev_res[len(rev_res)-1][1],rev_res[len(rev_res)-1][0])




       