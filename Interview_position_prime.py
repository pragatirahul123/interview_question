num=int(input("enter a position: "))
position=0
index=1
while True:
    c=0
    j=2
    while j<=index:
        if index%j==0:
            c=c+1
        j=j+1
    if c==1:
        position=position+1
        if position==num:
            print(index)
            break
    index=index+1
