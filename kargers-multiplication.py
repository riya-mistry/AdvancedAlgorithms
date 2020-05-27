def func(n1,n2):

	n1=str(n1)
	n2=str(n2)
	if len(n1) >= len(n2):
		for i in range(len(n1)-len(n2)):
			n2='0'+n2
	elif len(n2)>=len(n1):
		for i in range(len(n2)-len(n1)):
			n1='0'+n1
	if len(n1)==1:
		return int(n1)*int(n2),1
	elif len(n1)==len(n2) and int(n1) /2>=0:
		w=int(n1[:len(n1)/2])
		x=int(n1[(len(n1)/2):])
		y=int(n2[:len(n2)/2])
		z=int(n2[(len(n2)/2):])
		r,c1=func((w+x),(y+z))
		p,c2=func(w,y)
		q,c3=func(x,z)
		return ((pow(10,len(n1))*p)+(pow(10,len(n1)/2)*(r-p-q))+q),c1+c2+c3

if __name__=='__main__':
	x=int(input())
	y=int(input())
	print(func(x,y))
 
