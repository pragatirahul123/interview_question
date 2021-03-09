column=int(input("enter a number"))
row=int(input("enter a number"))
index=0
new=[]
while index<(row):
    new2=[]
    j=0
    while j<(column):
        a = index* j
        new2.append(a)
        j=j+1
    index=index+1
    new.append(new2)
print(new)

        

        



    





