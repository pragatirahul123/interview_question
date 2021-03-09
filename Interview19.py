num=int(input("enter a number"))
var=0
index=1
while True:
	c=0
	j=2
	while j<=index:
		if index%j==0:
			c=c+1
		j=j+1
	if c==1:
		print(index) 
		var=var+1
	if var==num:
		break
	index=index+1
