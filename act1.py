def powof2(n):
    if n==0:
        return 0
    if(n&(~(n-1)))==n:
        return 1
    return 0
    


num=int(input("enter number"))
if powof2(num):
    print(num,"is power of 2 ")
else:
    print(num,"is not powwer of 2")