num=int(input("enter a number"))
pos=0
index=1
while index<=num:
    c=0
    j=2
    while j<=index:
        if index%j==0:
            c=c+1
        j=j+1
    if c==1:
        pos=pos+1
        if index==num:
            print("position" ,pos)
    index=index+1


