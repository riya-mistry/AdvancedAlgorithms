import random
def power(x, y, p) : 
    res = 1    
    x = x % p  
  
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % p
        y = y >> 1      
        x = (x * x) % p        
    return res 
    
def gcd(x,y):
	while(y):
		x,y=y,x %y
	return x
def check_prime(n):
	k=20
	if n==2:
		return True
	if n ==0  or n%2==0:
		return False
	else:
		for i in range(0,k):
			a = random.randrange(2, n-2)
			if gcd(a,n) ==1:
				if power(a,n-1,n) != 1:
					return False
	return True
		


if __name__=="__main__":
	n = long(input())
	if check_prime(n):
		print("prime")
	else:
		print("composite")
