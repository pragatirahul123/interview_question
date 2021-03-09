list=[1,2,3,4,5,6,7,8,9,10]
index=0
count=0
count1=0
new1=[]
new2=[]
var=[]

while index<len(list):
    if list[index]%2==0:
        count=count+1
        new1.append(list[index])
    
    else:
        count1=count1+1
        new2.append(list[index])
    index=index+1
var=(["even",count,new1,["odd",count1,new2]])
print([var])




        
