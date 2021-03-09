num=int(input("enet"))
index=1
dic={}
while index<=num:
    j=1
    var=0
    empyt=[]
    while j<=10:
        var=index*j
        empyt.append(var)
        j=j+1
    dic[index]=empyt
    index=index+1
print(dic)

    
    
