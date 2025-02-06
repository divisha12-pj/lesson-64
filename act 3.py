def powofx(x,y):
    result=1
    while (y>0):
        if (y%2==0):
            x=x*x
            y>>=1
        else:
            result=result*x
            y=y-1

    return result
x=int(input("enter value of x"))
y=int(input("enter value of y"))
print("{} to power of {} is {}".format(x,y,powofx(x,y)))