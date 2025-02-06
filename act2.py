#power of 4
def powof4(n):
    count=0
    if n==0:
        return 0
    if (n&(~(n&(n-1)))):
        while (n>1):
            n>>=1
            count+=1
    
    if count%2==0:
        return 1
    else:
        return 0

num=int(input("enter number")) 
if powof4(num):
    print(num,"is power of 4")
else:
    print(num,"is not power of 4")

    