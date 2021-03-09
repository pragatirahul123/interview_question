def median(*num):
    if a>b:
        if a<c:
            median=a
            print(median)
        elif b>c:
            median=b
            print(median)
        else:
            median=c
            print(median)
    else:
        if a>c:
            median=a
        elif b<c:
            median=b
        else:
            median=c
    print(median)
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
median(a,b,c)


