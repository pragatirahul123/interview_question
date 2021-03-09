user=input("enter a string:")
var=user.split()
var.sort()
i=0
while i<len(var):
    i=i+1
#print(var)
a=''.join(var)
print(a)
b='-'.join(a)
print(b)



